from multiprocessing import Process
from multiprocessing import Queue
from datetime import datetime
import time

class server(Process):
    def __init__(self, read_q, write_q):
        super(server, self).__init__()
        self.input_q = read_q
        self.output_q = write_q

    def run(self):
        while True:
            msg = self.input_q.get()
            self.output_q.put(msg)

class client(Process):
    def __init__(self, read_q, write_q):
        super(client, self).__init__()
        self.input_q = read_q
        self.output_q = write_q

    def run(self):
        msg = "Hello!"
        msg_cnt = 0
        msg_measure = 50000
        t_meas = datetime.now()
        while True:
            self.output_q.put(msg)
            msg = self.input_q.get()

            msg_cnt += 1
            if msg_cnt % msg_measure == 0:
                t_delta = datetime.now() - t_meas
                msg_sec = msg_measure / t_delta.total_seconds()
                t_per_msg = 100000.0 * t_delta.total_seconds() / msg_measure
                print("{} msgs took {} seconds or {} us per msg or {} msgs/sec.".format( 
                        msg_measure,
                        t_delta.total_seconds(),
                        t_per_msg,
                        msg_sec))

                t_meas = datetime.now()

if __name__ == '__main__':
    server_input_q = Queue()
    server_output_q = Queue()
    aserver = server(server_input_q, server_output_q)
    aclient = client(server_output_q, server_input_q)
    aserver.start()
    aclient.start()

    while True:
        time.sleep(10)
