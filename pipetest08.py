from datetime import datetime

def server(invalue):
     #print("Server - got invalue msg_cnt is ".format(msg_cnt))
     return invalue

def client():
     msg_cnt = 0
     msg_measure = 50000
     t_now = datetime.now()
     while True:
         #print("Client - Sending")
         result = server("hello server")
         #print("Client - Got ".format("result"))

         msg_cnt += 1
         if msg_cnt % msg_measure == 0:
             t_delta = datetime.now() - t_now
             us_per_msg = 1000000.0 * t_delta.total_seconds()/msg_measure
             msg_sec = 1000000 / us_per_msg
             print("{} Messages took {} which is {} us per round trip or {} per second".format(msg_measure, 
                             t_delta, us_per_msg, msg_sec))
             t_now = datetime.now()


client()
