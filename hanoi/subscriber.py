# Subscribers are created with ZMQ.SUB socket types.
# A zmq subscriber can connect to many publishers.
import sys
import zmq
import base64
import simplejson as json

port = "5563"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)


# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from server...")
#socket.connect("tcp://localhost:%s" % port)
socket.connect("tcp://127.0.0.1:%s" % port)

# Subscribes to all topics you can selectively create multiple workers
# that would be responsible for reading from one or more predefined topics
# if you have used AWS SNS this is a simliar concept
socket.subscribe("")

while True:
    # Receives a string format message
    print(socket.recv())

    #data = socket.recv()
    #dumps the json object into an element
    json_str = json.dumps(data)

    #load the json to a string
    #resp = json.loads(json_str)

    #print the resp
    #print (resp)
    #print(resp["payload"])


    #extract an element in the response
    #print(resp['payload'])
    #dataEncoded = base64.b64decode(socket.recv())
    #print(dataEncoded)

    # extract an element in the response
    #print (dataEncoded['name'])    
    #print (dataEncoded['value'])