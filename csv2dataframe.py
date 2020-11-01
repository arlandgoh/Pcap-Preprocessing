import shlex, subprocess
import os
from os import listdir
from random import sample
import numpy as np
import time

path_pcap_data = "./csv_0102/"   # Pcaps Directory
dirs = os.listdir(path_pcap_data)

header_list = ['frame_number','date','time', 'time_second', 'src', 'dst', 'sport', 'dport', 'frame_len', 'protocol', 'frame_protocol', 'info', 'sequence', 'TTL']
df_15_mins = []
times = []

for i in range(len(dirs)):
    
    t0= time.clock()
    
    if (i<10):
        index = "0" + str(i+0)
    else:
        index = str(i+0)
    df = pd.read_csv(os.path.join(path_pcap_data,"2020010213{index}00tshark1.csv".format(index = index)), names=header_list, sep=',', index_col="frame_number")
    df = df[['src','dst','sport','dport', 'protocol','frame_protocol', 'frame_len']].astype(str)
    df['sport'] = df['sport'].str.replace('.0', '')
    df['dport'] = df['dport'].str.replace('.0', '')
    df_15_mins.append(df)
    print(i+1, "Done!")
    
    t1 = time.clock() - t0
    times.append(t1)
    print("Time elapsed: ", t1, 'second')
    
df_15_mins = pd.concat(df_15_mins, ignore_index=True)
print("Dataframe is generated!")


