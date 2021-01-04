import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
pwm=GPIO.PWM(40, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(40, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(40, False)
    pwm.ChangeDutyCycle(0)
try:
    while True:
        SetAngle(90) 
        sleep(3)
        SetAngle(180)
        sleep(3)
        SetAngle(0)
        sleep(3)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()