import pyaudio
import numpy
import struct
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
CHUNK = 1024
RECORD_SECONDS = 3

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("recording...")

frames = []
result_arr = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(numpy.frombuffer(data))
    data_int = numpy.array(struct.unpack(str(2*CHUNK) + 'B', data))[::2]
    result_arr.append(data_int)

# numpydata = numpy.hstack(frames)

#plotting last tuple
plt.plot(numpy.arange(0, len(data_int)), data_int)
plt.show()

print("finished recording")
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
