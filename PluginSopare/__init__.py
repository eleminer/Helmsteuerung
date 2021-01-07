from flask import Flask
from flask import request
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import time
def run(readable_results, data, rawbuf):
    if "live" in readable_results: 
        print("Livebild angeschaltet")
    if "aus" in readable_results: 
        print("Livebild ausgeschaltet")
    if "auf" in readable_results: 
        print("Servo auf")
    if "zu" in readable_results: 
        print("Servo zu")
def printTest():
    print("hello")
    sleep(1)

with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(printTest)
        executor.submit(run)
        executor.shutdown(wait=False)

