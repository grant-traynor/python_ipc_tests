from threading import Thread
from queue import Queue
from datetime import datetime
import time
from collections import deque

server_write_q = deque()
server_read_q = deque()

class server(Thread):
    def run(self):
        while True:
            try:
                msg = server_read_q.popleft()
            except IndexError:
                time.sleep(0)
                continue

            server_write_q.append(msg)

class client(Thread):
    def run(self):
        msg = "Hello!"
        msg_cnt = 0
        msg_measure = 50000
        t_meas = datetime.now()
        while True:
            server_read_q.append(msg)
            try:
                msg = server_write_q.popleft()
            except IndexError:
                time.sleep(0)
                continue
            msg_cnt += 1

            if msg_cnt % msg_measure == 0:
                t_delta = datetime.now() - t_meas
                msg_sec = msg_measure / t_delta.total_seconds()
                t_per_msg = 100000 * t_delta.total_seconds() / msg_measure
                print("{} msgs took {} seconds or {} us per msg or {} msgs/sec.".format( 
                        msg_measure,
                        t_delta.total_seconds(),
                        t_per_msg,
                        msg_sec))

                t_meas = datetime.now()
                

if __name__ == '__main__':
    aserver = server()
    time.sleep(1)
    aclient = client()
    aserver.start()
    aclient.start()

    while True:
        time.sleep(10)
