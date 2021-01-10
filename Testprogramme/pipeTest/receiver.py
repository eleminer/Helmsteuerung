import os
import select
from message import decode_msg_size

def get_message(fifo: int) -> str:
    msg_size_bytes = os.read(fifo, 4)
    msg_size = decode_msg_size(msg_size_bytes)
    msg_content = os.read(fifo, msg_size).decode("utf8")
    return msg_content


if __name__ == "__main__":
    IPC_FIFO_NAME = "/home/pi/sopareplugin_ipc"
    os.mkfifo(IPC_FIFO_NAME)
    try:
        fifo = os.open(IPC_FIFO_NAME, os.O_RDONLY | os.O_NONBLOCK)
        try:
            poll = select.poll()
            poll.register(fifo, select.POLLIN)
            try:
                while True:
                    if (fifo, select.POLLIN) in poll.poll(2000):
                        msg = get_message(fifo)
                        print(msg)
            finally:
                poll.unregister(fifo)
        finally:
            os.close(fifo)
    finally:
        os.remove(IPC_FIFO_NAME)