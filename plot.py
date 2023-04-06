import matplotlib.pyplot as plt
import numpy as np

aud = np.array([284996, 384918, 239032])
time_aud = np.array([55.43330907821655, 82.75282907485962, 45.20645308494568])
vid = np.array([8223213, 7299585, 7691948])
time_vid = np.array([72.58127403259277, 64.62296891212463, 64.66949319839478])

aud2 = [128041, 273259, 208086]
time_aud2 = [30.60102105140686, 60.84252619743347, 49.38770508766174]
vid2 = [14599354, 10921109, 13843576]
time_vid2 = [56.43308401107788, 42.14982080459595, 54.24628305435181]

audio = np.divide(aud, time_aud) * 60
video = np.divide(vid, time_vid) * 60

mean_audio = np.sum(audio) / 3
mean_video = np.sum(video) / 3

audio2 = np.divide(aud2, time_aud2) * 60
video2 = np.divide(vid2, time_vid2) * 60

mean_audio2 = np.sum(audio2) / 3
mean_video2 = np.sum(video2) / 3

tot = np.concatenate((audio,video))
print(mean_audio)
print(mean_audio2)
print(mean_video)
print(mean_video2)
x_labels = ['audio', 'video']

x = np.arange(len(x_labels))

plt.bar('audio même wifi', mean_audio, label='Appel audio sur même réseau wifi')
plt.bar('audio', mean_audio2, label='Appel audio sur réseau wifi different', color='aqua')
plt.bar('video même wifi', mean_video, label='Appel vidéo sur même réseau wifi', color='r')
plt.bar('vidéo', mean_video2, label='Appel vidéo sur réseau wifi different', color='darkorange')
plt.title("Débit en fonction de type d'appel")
plt.legend()

plt.ylabel('Débit - [Bytes/min]')
plt.savefig("Débit en fonction du type d'appel.pdf")
plt.show()