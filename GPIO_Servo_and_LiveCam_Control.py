import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ispressed20=0
ispressed16=0

touchTime20= int(round(time.time() * 1000))
touchTime16= int(round(time.time() * 1000))
millis=0
def getMillis():
    global millis
    millis= int(round(time.time() * 1000))

while True:
    getMillis()
    input_state20 = GPIO.input(20)
    if input_state20 == False and ispressed20==0:
        print('working1')
        touchTime20= int(round(time.time() * 1000))
        ispressed20=1
        
    elif input_state20==True and millis-touchTime20>500 :
        ispressed20=0
    
    input_state16 = GPIO.input(16)
    if input_state16 == False and ispressed16==0:
        print('working2')
        touchTime16= int(round(time.time() * 1000))
        ispressed16=1
    elif input_state16==True and millis-touchTime16>500:
        ispressed16=0

    