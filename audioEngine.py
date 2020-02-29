import pyaudio
import numpy
import struct

def generateAudioChunks(**kwargs):
    '''
    params:
        RATE: Sampling rate for audio signals (8000)
        TIME: Time to record in seconds
    '''
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=kwargs["RATE"], input=True,
                        frames_per_buffer=512)

    for i in range(0, int(kwargs["RATE"] / 512 * kwargs["TIME"])):
        data = stream.read(512)
        data_int = numpy.array(struct.unpack(
            str(2*512) + 'B', data))[::2]
        yield data_int

    stream.stop_stream()
    stream.close()
    audio.terminate()
