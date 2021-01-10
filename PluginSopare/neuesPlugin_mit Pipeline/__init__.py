import os

def create_msg(content: bytes) -> bytes:
    size = len(content)
    return encode_msg_size(size) + content

def pipesend(name):
    IPC_FIFO_NAME = "/home/pi/sopareplugin_ipc"
    fifo = os.open(IPC_FIFO_NAME, os.O_WRONLY)
    content = str(name).encode("utf8")
    msg = create_msg(content)
    os.write(fifo, msg)
    os.close(fifo)

def run(readable_results, data, rawbuf):
    if "live" in readable_results:
        pipesend("live")
    if "aus" in readable_results:
        pipesend("aus") 
    if "auf" in readable_results: 
        pipesend("auf")
    if "zu" in readable_results: 
        pipesend("zu")
    


