from threading import Thread
from queue import Queue
from datetime import datetime
import time

server_write_q = Queue()
server_read_q = Queue()

class server(Thread):
    def run(self):
        while True:
            msg = server_read_q.get()
            server_write_q.put(msg)

class client(Thread):
    def run(self):
        msg = "Hello!"
        msg_cnt = 0
        msg_measure = 50000
        t_meas = datetime.now()
        while True:
            server_read_q.put(msg)
            msg = server_write_q.get()
            msg_cnt += 1

            if msg_cnt % msg_measure == 0:
                t_delta = datetime.now() - t_meas
                msg_sec = msg_measure / t_delta.total_seconds()
                t_per_msg = 100000 * t_delta.total_seconds() / (msg_measure)
                print("{} msgs took {} seconds or {} us per msg or {} msgs/sec.".format( 
                        msg_measure,
                        t_delta.total_seconds(),
                        t_per_msg,
                        msg_sec))

                t_meas = datetime.now()
                

if __name__ == '__main__':
    aserver = server()
    aclient = client()
    aserver.start()
    aclient.start()

    while True:
        time.sleep(10)
