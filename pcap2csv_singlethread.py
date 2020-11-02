import shlex, subprocess
import os
from os import listdir
from random import sample
import numpy as np
import time

path_pcap_data = "./pcap"
dirs = os.listdir(path_pcap_data)

header_list = ['frame_number','date','time', 'time_second', 'src', 'dst', 'sport', 'dport', 'frame_len', 'columns_len', 'protocol', 'occurence']
df_15_mins = []
times = []

for i in range(len(dirs)):
    t0= time.perf_counter()
    if (i<9):
        index = "0" + str(i+1)
        
    else:
        index = str(i+1)

    x = "tshark -r 2020010113{}00.pcap -T fields -e frame.number -e frame.time -t e -e _ws.col.Time -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e frame.len -e _ws.col.Length -e _ws.col.Protocol -e frame.protocols -e _ws.col.Info -E separator=, -E occurrence=f > 2020010113{}00tshark1.csv".format(index, index)
    p = subprocess.call(x, shell=True)

    print(i+1, "Done!")
    t1 = time.perf_counter() - t0
    times.append(t1)
    print("Time elapsed: ", t1, 'second')
    


