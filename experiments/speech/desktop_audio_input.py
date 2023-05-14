import pyaudio
import wave

fileIndex=0
while True:
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 60
    WAVE_OUTPUT_FILENAME = f"./saved_audio/output{fileIndex}.wav"

    p = pyaudio.PyAudio()
    input_index = None
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if dev['maxInputChannels'] > 0 and 'Stereo Mix' in dev['name']:
            input_index = i
            break
    
    #DESKTOP AUDIO
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=input_index,
                    frames_per_buffer=CHUNK)

    frames = []

    print(f"Recording... {fileIndex}")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print(f"Finished recording {fileIndex}")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    fileIndex+=1