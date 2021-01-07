def run(readable_results, data, rawbuf):
    f = open("/home/pi/Downloads/arguments.txt", "w")
    if "live" in readable_results: 
        print("Livebild angeschaltet")
        f.write("live")
    if "aus" in readable_results: 
        print("Livebild ausgeschaltet")
        f.write("aus")
    if "auf" in readable_results: 
        print("Servo auf")
        f.write("auf")
    if "zu" in readable_results: 
        print("Servo zu")
        f.write("zu")
    f.close()

