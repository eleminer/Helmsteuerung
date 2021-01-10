from flask import Flask
from flask import request
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import os
from concurrent.futures import ThreadPoolExecutor
import time
from subprocess import Popen
import subprocess
import select
from message import decode_msg_size
from subprocess import Popen, PIPE, CalledProcessError
os.environ["DISPLAY"] = ':0'
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
argument="On"
image = Popen(["feh", "--hide-pointer", "-x", "-q", "-B", "black", "/home/pi/Helmsteuerung/PopUpFenster/speech"+str(argument)+".jpg"])


try:
    app = Flask(__name__)

    def get_message(fifo: int) -> str:
        msg_size_bytes = os.read(fifo, 4)
        msg_size = decode_msg_size(msg_size_bytes)
        msg_content = os.read(fifo, msg_size).decode("utf8")
        return msg_content

    def pipeline():
        global livefeed,argument,servoposition
        print("pipeline started")
        with Popen(['python3', '-u', 'receiver.py'], stdout=PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                print(line, end='') # process line here
                if "live" in str(line) and argument=="On":
                    print("live from text")
                    livefeed=0
                    live()
     
                if "aus" in str(line) and argument=="On":
                    print("aus from text")
                    livefeed=1
                    live()
                                    
                if "auf" in str(line) and argument=="On":
                    print("auf from text")
                    servoposition=1
                    servo()
                                        
                if "zu" in str(line) and argument=="On":
                    print("zu from text")
                    servoposition=0
                    servo()
                
        if p.returncode != 0:
            raise CalledProcessError(p.returncode, p.args)

        if "live" in str(msg) and argument=="On":
            print("live from text")
            livefeed=0
            live()
     
        if "aus" in str(msg) and argument=="On":
            print("aus from text")
            livefeed=1
            live()
                               
        if "auf" in str(msg) and argument=="On":
            print("auf from text")
            servoposition=1
            servo()
                                
        if "zu" in str(msg) and argument=="On":
            print("zu from text")
            servoposition=0
            servo()
                
    def speechSwitch():
        global argument
        if argument=="On":
            argument="Off"
        else:
            argument="On"
        showImage()

    def showImage():
        global argument, image
        image.terminate()
        subprocess.call(["xdotool", "mousemove", "945", "132"])
        image = Popen(["feh", "--hide-pointer", "-x", "-q", "-B", "black", "/home/pi/Helmsteuerung/PopUpFenster/speech"+str(argument)+".jpg"])
               
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
        print("app")
        @app.route('/SB')
        def SB():
            AppData = request.args.get('Data')
            print(AppData)
            if AppData=="2":
                servo()
            if AppData=="1":
                live()
            if AppData=="3":
                speechSwitch()
            return "ok!"
        app.run(host='0.0.0.0', port= 8090)

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(gpio)
        executor.submit(appControl)
        executor.submit(pipeline)
        executor.shutdown(wait=False)
    

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()