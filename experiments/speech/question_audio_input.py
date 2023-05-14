import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "question.wav"

def ask_ques():
    print("Listening to question...")
    p = pyaudio.PyAudio()
    input_index = None
    # for i in range(p.get_device_count()):
    #     dev = p.get_device_info_by_index(i)
    #     print("device1:",dev)
        # if dev['maxInputChannels'] > 0 and 'Microphone' in dev['name']:
        #     input_index = i
        #     break
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=3,
                    frames_per_buffer=CHUNK)

    max_range = int(RATE / CHUNK * RECORD_SECONDS)

    print("* recording")

    frames = []

    for i in range(0, max_range):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()