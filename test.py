import sounddevice as sd
import numpy as np

fs = 44100
data = np.random.uniform(-1,1,fs) # 44100 random samples between -1 and 1
scaled = np.int16(data/np.max(np.abs(data)) * 32767)
sd.play(scaled, fs)
