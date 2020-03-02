import pyaudio
import numpy
import struct

CHUNK = 2048

def generateAudioChunks(**kwargs):
    '''
    params:
        RATE: Sampling rate for audio signals (8000)
    '''
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=kwargs["RATE"], input=True,
                        frames_per_buffer=CHUNK)

    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        data_int = numpy.array(struct.unpack(
            str(2*CHUNK) + 'B', data))[::2]
        yield data_int
