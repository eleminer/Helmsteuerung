import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

camera = PiCamera()
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

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()