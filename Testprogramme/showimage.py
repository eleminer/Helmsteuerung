import subprocess
import os
os.environ["DISPLAY"] = ':0'
subprocess.call(["xdotool", "mousemove", "945", "132"])
image = subprocess.call(["feh", "--hide-pointer", "-x", "-q", "-B", "black", "/home/pi/Downloads/speechOn.jpg"])
image.kill()