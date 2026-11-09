import pyaudio
import numpy
import matplotlib.pyplot as plt
FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220
p = pyaudio.PyAudio()
print("running")
stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,
input=True,frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = numpy.frombuffer(data, dtype=numpy.int16);
stream.stop_stream()
stream.close()
p.terminate()
numpy.save("audio",decoded)
print("done")

l = numpy.load("data/audio.npy")
print(l)
plt.plot(decoded)
plt.show()