import math
# подключение массивов
import numpy as np
# чтение wav файлов
import scipy.io.wavfile as wavfile
# графики
import matplotlib.pyplot as plt
# rate - частота дискретизации данных      data - массив амплитуд
rate, data = wavfile.read('breathe.wav')
# длительность одного столбика date 
time = np.arange(len(data[:]))*1.0/rate


print(data)

# количество средних чисел
framesize = 1000
if(framesize <= 0):
	framesize = 1
new = []

#frame = sum(data[:framesize / 2]) / (framesize / 2)
#new.append(frame)
if(len(data) >= framesize):
	miniframesize = 0
	frame = 0
	for i in range(len(data) - int(framesize / 2)):
		frame = sum(data[i:i+framesize / 2])
		if(i <= framesize / 2):
			miniframesize = len(data[:i]) + framesize / 2
			frame += sum(data[:i])
		else:
			miniframesize = framesize
			frame += sum(data[(i - framesize / 2):i])
		frame = frame / miniframesize
		new.append(frame)
	for i in range(len(data) - int(framesize / 2), len(data)):
		frame = sum(data[i - framesize / 2:i])
		if(i < len(data)):
			if(len(data) - i > framesize / 2):
				miniframesize = framesize
				frame += sumn(data[(i + 1):(i + framesize / 2 + 1)])
			else:
				miniframesize = framesize / 2 + len(data[i + 1:])
				frame += sum(data[(i + 1):])
		sframe = frame / miniframesize
		new.append(frame)
nparr = np.array(new)
wavfile.write("new_breathe_"+str(framesize)+".wav", rate, nparr)

plt.plot(time, data[:])
plt.plot(time, nparr[:], 'g')
plt.show()
