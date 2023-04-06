import pyshark
import matplotlib.pyplot as plt
import numpy as np

cap = pyshark.FileCapture('Analyse_debit_pas_meme_wifi/audio_vers_video.pcap')

data_rates = []
times = []
previous_time = None
for packet in cap:
    packet_time = float(packet.sniff_time.timestamp())
    if previous_time:
        time_interval = packet_time - previous_time
        if time_interval == 0:
            pass
        else:
            data_rate = int(packet.length) / time_interval
            data_rates.append(data_rate)
            times.append(packet_time)
    previous_time = packet_time

arr1 = np.array(times)
arr = np.subtract(arr1, arr1[0])
print(arr[0])
print(arr[-1])
x = np.linspace(0, arr[-1], len(data_rates))
plt.plot(x, data_rates)
plt.ylabel('Data Rate (bytes/s)')
plt.xlabel('packet number')
plt.show()

window_size = 5
meand_data_rates = np.convolve(data_rates, np.ones(window_size)/window_size, mode='valid')
mean_times = arr[window_size - 1:]

plt.plot(mean_times, meand_data_rates)
plt.ylabel('Meand Data Rate (bytes/s)')
plt.xlabel('Time (seconds)')
plt.title("Débit en fonction du temps")
plt.savefig("Debit en fonction du temps.pdf")
plt.show()