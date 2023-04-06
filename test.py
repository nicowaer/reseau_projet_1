import pyshark
import matplotlib.pyplot as plt
import numpy as np


time_vid = []
time_aud= []
aud =  []
vid = []
for i in range(1,4):

    str1 = "Analyse_debit/audio{}.pcap".format(i)
    str2 = "Analyse_debit/video{}.pcap".format(i)
    cap_aud = pyshark.FileCapture(str1)
    cap_vid = pyshark.FileCapture(str2)

    first_packet_time_aud = None
    last_packet_time_aud = None
    total_aud = 0
    first_packet_time_vid = None
    last_packet_time_vid = None
    total_vid = 0

    for packet in cap_aud:
        total_aud += int(packet.length)
        if first_packet_time_aud is None:
            first_packet_time_aud = float(packet.sniff_time.timestamp())
        last_packet_time_aud = float(packet.sniff_time.timestamp())
    time_aud.append(last_packet_time_aud - first_packet_time_aud)
    aud.append(total_aud)
    cap_aud.close()

    for packet1 in cap_vid:
        total_vid += int(packet1.length)
        if first_packet_time_vid is None:
            first_packet_time_vid = float(packet1.sniff_time.timestamp())
        last_packet_time_vid = float(packet1.sniff_time.timestamp())
    time_vid.append(last_packet_time_vid - first_packet_time_vid)
    vid.append(total_vid)
    cap_vid.close()

print(aud)
print(time_aud)
print(vid)
print(time_vid)


