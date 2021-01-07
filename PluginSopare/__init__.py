import time
def run(readable_results, data, rawbuf):
    if "live" in readable_results: 
        print("Livebild angeschaltet")
        file = open('/home/pi/Downloads/'+str(1)+'.txt','w')
        file.write("live\r")
        file.close()
    if "aus" in readable_results: 
        print("Livebild ausgeschaltet")
        file = open('/home/pi/Downloads/'+str(1)+'.txt','w')
        file.write("aus\r")
        file.close()
    if "auf" in readable_results: 
        print("Servo auf")
        file = open('/home/pi/Downloads/'+str(1)+'.txt','w')
        file.write("auf\r")
        file.close()
    if "zu" in readable_results: 
        print("Servo zu")
        file = open('/home/pi/Downloads/'+str(1)+'.txt','w')
        file.write("zu\r")
        file.close()
    


