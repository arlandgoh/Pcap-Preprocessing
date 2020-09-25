import shlex, subprocess
import os
from os import listdir
from random import sample
import numpy as np
import time

pcap_filename = input("Please enter pcap file name: ")
print("Generating 15 smaller pcap files...")
x = "editcap -i 60 {filename}.pcap 60secs.pcap".format(filename = pcap_filename)

def subprocess_cmd(command):
    subprocess.call(command, shell=True)
    # os.popen("editcap -i 60 202001011400.pcap 60secs.pcap")

subprocess_cmd(x)
print("Completed.")


