# Copyright (c) 2021 Intel Corporation.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""EIS Message Bus publisher example
"""

import time
import json
import argparse
import numpy as np
import eis.msgbus as mb

# Argument parsing
ap = argparse.ArgumentParser()
ap.add_argument('config', help='JSON configuration')
ap.add_argument('-t', '--topic', default='events', help='Topic')
ap.add_argument('-b', '--blob_size', type=int, default=10,
                help='Number of bytes for the blob')
ap.add_argument('-i', '--interval', type=float, default=1,
                help='Interval between each publication')
args = ap.parse_args()

msgbus = None
publisher = None

with open(args.config, 'r') as f:
    config = json.load(f)

try:
    print('[INFO] Initializing message bus context')
    msgbus = mb.MsgbusContext(config)

    print(f'[INFO] Initializing publisher for topic \'{args.topic}\'')
    publisher = msgbus.new_publisher(args.topic)

    print('[INFO] Running...')

    #dat = np.fromfile("iqsamples.float32", dtype="float32")
    dat = np.fromfile("parrotdrone_ON_2_412GHz_GAIN_0_0_0_RFSHIELDOPEN_xab_05272020_rfdata.dat", dtype="float32")

    N = len(dat)
    i = 0    
    while(i < N):
       # proccess data, dat[0] = I-Value  dat[1] = Q-Value

       # numpy.float32 -> python float, to make numpy.float32 object serializable, for example
       # val = np.float32(0)
       # pyval = val.item()
       payloadi = dat[i].item()
       payloadq = dat[i+1].item()
       iqdata = {
          'idata': payloadi,
          'qdata': payloadq
       }
       print("Sending values: I-Value %s, Q-Value %s" % (payloadi, payloadq))
       publisher.publish(iqdata)

       i += 1

except KeyboardInterrupt:
    print('[INFO] Quitting...')
finally:
    if publisher is not None:
        publisher.close()
