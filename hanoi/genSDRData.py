
import requests
import json
import random
import time
import numpy as np


edgexip = '127.0.0.1'
ival = 0
qval = 0

'''
def generateSensorData(ival, qval):

    #ival = random.randint(humval-5,humval+5)
    #qval = random.randint(tempval-1, tempval+1)

    print("Sending values: I-Value %s, Q-Value %s" % (ival, qval))

    return (ival, qval)
'''


if __name__ == "__main__":

    #dat = np.fromfile("iqsamples.float32", dtype="float32")
    dat = np.fromfile("parrotdrone_ON_2_412GHz_GAIN_0_0_0_RFSHIELDOPEN_xab_05272020_rfdata.dat", dtype="float32")

    N = len(dat)
    i = 0    
    while(i < N):

       # proccess data, dat[0] = I-Value  dat[1] = Q-Value
       url = 'http://%s:49986/api/v1/resource/I_and_Q_SDR_sensor_01/ivalue' % edgexip


# for example, numpy.float32 -> python float
#val = np.float32(0)
#pyval = val.item()
       payloadi = dat[i].item()
       headers = {'content-type': 'application/json'}
       response = requests.post(url, data=json.dumps(payloadi), headers=headers, verify=False)

       url = 'http://%s:49986/api/v1/resource/I_and_Q_SDR_sensor_01/qvalue' % edgexip
       payloadq = dat[i+1].item()
       headers = {'content-type': 'application/json'}
       response = requests.post(url, data=json.dumps(payloadq), headers=headers, verify=False)

       print("Sending values: I-Value %s, Q-Value %s" % (payloadi, payloadq))
       
       time.sleep(1)
       i += 1
