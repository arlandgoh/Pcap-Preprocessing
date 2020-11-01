# Introduction to Predictive Security Analytics

## Pcap Multi-threading Preprocessing Micro-services

We're looking for most effective way to pre-process pcap traces. Feel free to contact me for discussion and collaboration. 

## Description

The modules can be used for pcap-csv conversion.

1. pcap2pcaps - using editcap to split a large pcap file into smaller pcap files.
2. pcap2csv_singlethread - using tshark to extract the important field from pcap files.
3. pcap2csv5_multithreads_3 - using tshark and multithreading (3 threads) to extract the important field from pcap files.
4. pcap2csv5_multithreads_5 - using tshark and multithreading (5 threads) to extract the important field from pcap files.
5. csv2dataframe - using Pandas to read in csv files and concatenate all the dataframe into one.