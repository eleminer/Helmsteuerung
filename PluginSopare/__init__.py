from flask import Flask
from flask import request
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
from concurrent.futures import ThreadPoolExecutordef run(readable_results, data, rawbuf):
    print readable_results
    if "live" in readable_results: 
        print("Livebild angeschaltet")
    if "aus" in readable_results: 
        print("Livebild ausgeschaltet")
    if "auf" in readable_results: 
        print("Servo auf")
    if "zu" in readable_results: 
        print("Servo zu")