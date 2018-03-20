import asyncio
import uvloop
from datetime import datetime

@asyncio.coroutine
async def server(invalue):
     #print("Server - got invalue msg_cnt is ".format(msg_cnt))

     yield invalue

@asyncio.coroutine
async def client():
     msg_cnt = 0
     msg_measure = 50000
     t_now = datetime.now()
     while True:
         #print("Client - Sending")
         result = await server("hello server")
         #print("Client - Got ".format("result"))

         msg_cnt += 1
         if msg_cnt % msg_measure == 0:
             t_delta = datetime.now() - t_now
             us_per_msg = 1000000.0 * t_delta.total_seconds()/msg_measure
             msg_sec = 1000000 / us_per_msg
             print("{} Messages took {} which is {} us per round trip or {} per second".format(msg_measure, 
                             t_delta, us_per_msg, msg_sec))
             t_now = datetime.now()

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()
loop.run_until_complete(client())

loop.close()
