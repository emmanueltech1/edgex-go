# Subscribers are created with ZMQ.SUB socket types.
# A zmq subscriber can connect to many publishers.
import sys
import zmq
import base64
import simplejson as json
import io
import eis.msgbus as mb

raw_payload = ""
ivalue = 0
qvalue = 0

port = "5563"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

msgbus = None
subscriber = None

with open("../../examples/configs/tcp_subscriber_no_security.json", 'r') as sf:
    subconfig = json.load(sf)

print('[INFO] Initializing message bus context')
submsgbus = mb.MsgbusContext(subconfig)

print(f'[INFO] Initializing subscriber for topic')
subscriber = submsgbus.new_subscriber("events")

with open("../../examples/configs/mytcp_publisher_no_security.json", 'r') as pf:
    pubconfig = json.load(pf)

print('[INFO] Initializing message bus context')
pubmsgbus = mb.MsgbusContext(pubconfig)

print(f'[INFO] Initializing publisher for topic \'i-q-data\'')
publisher = pubmsgbus.new_publisher("i-q-data")

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
    #print(socket.recv())

    data = socket.recv()
    #dumps the json object into an element
    json_str = json.dumps(data)
    print ("json_str:",json_str)

    #load the json to a string
    #resp = json.loads(json_str)

    #print the resp
    #print ("resp:", resp)
    payload_index_offset = 12
    result_start_payload_index = json_str.find('Payload') 
    print ("Substring 'payload' found at index:", result_start_payload_index)

    result_end_payload_index = json_str.find('\"', result_start_payload_index+payload_index_offset) 
    print ("Substring '\"' found at index:", result_end_payload_index)
    
    raw_payload = json_str[result_start_payload_index+payload_index_offset:result_end_payload_index-1]
    if result_start_payload_index > -1: 
        print ("json_str - payload: ", json_str[result_start_payload_index+payload_index_offset:result_end_payload_index-1])
        raw_payload = json_str[result_start_payload_index+payload_index_offset:result_end_payload_index-1]
        dataEncoded = base64.b64decode(raw_payload)
        print(dataEncoded)
        fix_bytes_value = dataEncoded.replace(b"'", b'"')
        my_json = json.load(io.BytesIO(fix_bytes_value)) 
        # extract an element in the response
        pairs = my_json.items()

        for key, value in pairs:
            print(key, value)
            if key == "readings":
                print("value[0][name] ",value[0]['name'])
                if value[0]['name'] == "ivalue":
                    print("value[0][value] - I:",value[0]['value'])
                    ivalue = float(value[0]['value'])
                    print("ivalue: ",ivalue)
                if value[0]['name'] == "qvalue":
                    print("value[0][value] - Q:",value[0]['value'])
                    qvalue = float(value[0]['value'])
                    print("qvalue:",qvalue)

                iqdata = {
                    'idata': ivalue,
                    'qdata': qvalue
                }
       
                print("Sending values: I-Value %s, Q-Value %s" % (ivalue, ivalue))
                publisher.publish(iqdata)
    #extract an element in the response
    #print(resp['payload'])
    #dataEncoded = base64.b64decode(socket.recv())
    #dataEncoded = base64.b64decode(resp)
    #print(dataEncoded)

    # extract an element in the response
    #print (dataEncoded['name'])    
    #print (dataEncoded['value'])