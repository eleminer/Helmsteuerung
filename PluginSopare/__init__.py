import time
def run(readable_results, data, rawbuf):
    file = open('/home/pi/Downloads/'+str(int(round(time.time() * 1000)))+'.txt','w')
    if "live" in readable_results: 
        print("Livebild angeschaltet")
        file.write("live")
    if "aus" in readable_results: 
        print("Livebild ausgeschaltet")
        file.write("aus")
    if "auf" in readable_results: 
        print("Servo auf")
        file.write("auf")
    if "zu" in readable_results: 
        print("Servo zu")
        file.write("zu")
    
    file.close()


