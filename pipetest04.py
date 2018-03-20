import asyncio
import uvloop
from datetime import datetime

# The Client
class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
         self.msg_cnt = 0
         self.msg_measure = 50000
         self.message = message
         self.loop = loop
         self.t_now = datetime.now()
         print("Initing Client")

    def connection_made(self, transport):
         self.transport = transport
         self.transport.write(self.message.encode())
         #print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
         #print('Data received: {!r}'.format(data.decode()))
         self.transport.write(self.message.encode())
         self.msg_cnt += 1
         if self.msg_cnt % self.msg_measure == 0:
              t_delta = datetime.now() - self.t_now
              us_per_msg = 1000000.0 * t_delta.total_seconds()/self.msg_measure
              msg_sec = 1000000 / us_per_msg
              print("{} Messages took {} which is {} us per round trip or {} per second".format(self.msg_measure, 
                              t_delta, us_per_msg, msg_sec))
              self.t_now = datetime.now()


    def connection_lost(self, exc):
         print('The server closed the connection')
         print('Stop the event loop')
         self.loop.stop()

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        #print('Data received: {!r}'.format(message))

        #print('Send: {!r}'.format(message))
        self.transport.write(data)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()

# Setup the Server
coro = loop.create_unix_server(EchoServerClientProtocol, '/tmp/uds01')
server = loop.run_until_complete(coro)
print('Serving on {}'.format(server.sockets[0].getsockname()))

# Setup the Client
message = 'Hello World!'
client = loop.create_unix_connection(lambda: EchoClientProtocol(message, loop), '/tmp/uds01')
loop.run_until_complete(client)

# Serve requests until Ctrl+C is pressed
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

