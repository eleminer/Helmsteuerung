from flask import Flask
from flask import request
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import time

camera = PiCamera()
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)
pwm=GPIO.PWM(21, 50)
pwm.start(0)
servoposition = 1
livefeed = 0
ispressed20=0
ispressed16=0
touchTime20= int(round(time.time() * 1000))
touchTime16= int(round(time.time() * 1000))
millis=0


try:
    app = Flask(__name__)
    def readSpeechArguments():
        global livefeed servoposition
        f = open("/home/pi/Downloads/arguments.txt", "w")
        if "live" in f.read():
            live() 
        if "live" in f.read():
            livefeed=1
            live() 
        if "auf" in f.read():
            servoposition=1
            servo()
        if "zu" in f.read():
            servoposition=0
            servo()


    def getMillis():
        global millis
        millis= int(round(time.time() * 1000))

    def SetAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(21, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(21, False)
        pwm.ChangeDutyCycle(0)

    def servo():
        global servoposition
        if servoposition==1: #auf
            SetAngle(0)
            servoposition=0
        elif servoposition==0: #zu
            SetAngle(180)
            servoposition=1

    def live():
        global livefeed
        if livefeed==0:
            camera.start_preview()
            livefeed=1
        elif livefeed==1:
            camera.stop_preview()
            livefeed=0
    
    def gpio():
        global ispressed16,ispressed20,touchTime16,touchTime20
        while True:
            getMillis()
            input_state20 = GPIO.input(20)
            if input_state20 == False and ispressed20==0:
                servo()
                touchTime20= int(round(time.time() * 1000))
                ispressed20=1 
            elif input_state20==True and millis-touchTime20>500 :
                ispressed20=0
            
            input_state16 = GPIO.input(16)
            if input_state16 == False and ispressed16==0:
                live()
                touchTime16= int(round(time.time() * 1000))
                ispressed16=1
            elif input_state16==True and millis-touchTime16>500:
                ispressed16=0

    def appControl():
        @app.route('/SB')
        def SB():
            AppData = request.args.get('Data')
            print(AppData)
            if AppData=="2":
                servo()
            if AppData=="1":
                live()
            return "ok!"
        app.run(host='0.0.0.0', port= 8090)

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(gpio)
        executor.submit(appControl)
        executor.shutdown(wait=False)
    

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()