# Publishers are created with ZMQ.PUB socket types
# Data is published along with a topic.The subscribers usually
# sets a filter on these topics for topic of their interests.

# A publisher has no connected subscribers, then it will simply drop all messages.
# If you’re using TCP, and a subscriber is slow, messages will queue up on the publisher.
# In the current versions of ØMQ, filtering happens at the subscriber side, not the publisher side.

import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
#socket.bind("tcp://*:%s" % port)
socket.bind("tcp://127.0.0.1:%s" % port)


while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215) - 80
    print("%d %d" % (topic, messagedata))
    socket.send(b"%d %d" % (topic, messagedata))
    time.sleep(1)