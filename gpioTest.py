import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) #pullUp

while True:
    input_state = GPIO.input(20)
    if input_state == False: #if button connected to ground
        print('working')