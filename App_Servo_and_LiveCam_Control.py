from flask import Flask
from flask import request
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

camera = PiCamera()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
pwm=GPIO.PWM(40, 50)
pwm.start(0)
servoposition = 1
livefeed = 0

try:
    app = Flask(__name__)

    def SetAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(40, True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(40, False)
        pwm.ChangeDutyCycle(0)

    def servo():
        global servoposition
        if servoposition==1:
            SetAngle(0)
            servoposition=0
        elif servoposition==0:
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

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()