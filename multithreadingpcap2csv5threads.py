import shlex, subprocess
import os
from os import listdir
from random import sample
import random
import numpy as np
import time
import threading
from threading import Thread

def test_fn(thread_number, number_of_task):
    
    #path_pcap_data = "./pcap"
    #dirs = os.listdir(path_pcap_data)

    df_15_mins = []
    times = []

    for i in range(number_of_task):
        
        t0= time.perf_counter()
        if (thread_number == 1):
            if (i<3):
                index = "0" + str(i+1)
            else:
                index = str(i+1)
                
        elif(thread_number == 2):
            if (i<3):
                index = "0" + str(i+4)
            else:
                index = str(i+4)

        elif(thread_number == 3):
            if (i<3):
                index = "0" + str(i+7)
            else:
                index = str(i+7)

        elif(thread_number == 4):
            if (i<3):
                index = str(i+10) 
            else:
                print("opssss")

        elif(thread_number == 5):
            if (i<5):
                index = str(i+13)
            else:
                print("Error")
                
        x = "tshark -r 2020010113{}00.pcap -T fields -e frame.number -e frame.time -t e -e _ws.col.Time -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e frame.len -e _ws.col.Protocol -e frame.protocols -e _ws.col.Info -E separator=, -E occurrence=f > 2020010113{}00tshark1.csv".format(index, index)
        p = subprocess.call(x, shell=True)

        print(index, "Done!")
        t1 = time.perf_counter() - t0
        times.append(t1)
        print("Time elapsed: ", t1, 'second')

    print("Done!")

jobs = []
threads = 5
thread_number = [1,2,3,4,5]
number_of_task = [3,3,3,3,3]

for i in range(0, threads):  
    thread = Thread(target=test_fn, args=(thread_number[i], number_of_task[i]))
    thread.daemon = True
    jobs.append(thread)
       
for j in jobs:
    j.start()
      
for j in jobs:
    j.join()

