import sys
import os
from datetime import datetime

debug = False
norm_val = 1000000
endian = 'little'

args = sys.argv
if len(args) < 2:
    print('Usage:', args[0], '[csvFile]')
    exit()

path_in = args[1]
path_out = os.path.splitext(path_in)[0] + '.bin'
if not os.path.isfile(path_in):
    print('File not exist:', path_in)
    exit()

with open(path_in,'r') as src:    
    with open(path_out, 'wb') as dst:
        for line in src:
            datas = line.replace('\n','').split(',')              
            if len(datas) != 5:
                continue

            # get UNIX time as UTC
            if not '.' in datas[0]:
                datas[0] += '.000'
            datas[0] += ' +0000'
            t = datetime.strptime(datas[0], '%Y-%m-%d %H:%M:%S.%f %z').timestamp()
            
            # raw data
            t_unix = int(t)
            t_ms = round((t - t_unix) * 1000)
            ask = int(float(datas[1]) * norm_val)
            bid = int(float(datas[2]) * norm_val)
            ask_vol = int(datas[3])
            bid_vol = int(datas[4])
            
            # binary data
            t_unix_b = t_unix.to_bytes(4, endian)
            t_ms_b = t_ms.to_bytes(2, endian)
            ask_b = ask.to_bytes(4, endian)
            bid_b = bid.to_bytes(4, endian)
            ask_vol_b = ask_vol.to_bytes(4, endian)
            bid_vol_b = bid_vol.to_bytes(4, endian)
            
            if debug:
                print(datas)
                print(t_unix, t_ms, ask, bid, ask_vol, bid_vol)
                print(t_unix_b.hex(), t_ms_b.hex(), ask_b.hex(), bid_b.hex(), ask_vol_b.hex(), bid_vol_b.hex())
            
            dst.write(t_unix_b)
            dst.write(t_ms_b)
            dst.write(ask_b)
            dst.write(bid_b)
            dst.write(ask_vol_b)
            dst.write(bid_vol_b)
    