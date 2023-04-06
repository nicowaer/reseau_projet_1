import matplotlib.pyplot as plt
import numpy as np

aud = np.array([284996, 384918, 239032])
time_aud = np.array([55.43330907821655, 82.75282907485962, 45.20645308494568])
vid = np.array([8223213, 7299585, 7691948])
time_vid = np.array([72.58127403259277, 64.62296891212463, 64.66949319839478])

audio = np.divide(aud, time_aud) * 60
video = np.divide(vid, time_vid) * 60

tot = np.concatenate((audio,video))

x_labels = ['audio1', 'audio2', 'audio3', 'video1', 'video2', 'video3']
x_labels_2 = []

index = np.arange(len(x_labels)) + 0.1

bar_width = 0.35
x = np.arange(len(x_labels))
plt.bar(index, tot, width=bar_width, label='Audio')
#plt.bar(index, video, width=bar_width, label='Video')

plt.xlabel('Débit - [Bytes/min]')
plt.ylabel('Value')
plt.title('Bar plot')

plt.legend()
plt.show()

plot = plt.bar(x_labels, tot)
plot[3].set_color('r')
plot[4].set_color('r')
plot[5].set_color('r')

plt.ylabel('Débit - [Bytes/min]')
plt.show()