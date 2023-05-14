# MyReplica.ai - Building Your own Personal AI

## Part 1: Speech
[You can watch the Demo here](https://www.veed.io/view/b138cf39-abb9-48c9-9c35-80ddd7b48d58?panel=share)

Description: This part of the project tries to mimic the functionality of a personal AI that always listens to what you are listening to. You can play anything on your desktop, (run it for atleast a few minutes for better results) and OpenAI's whisper would convert all the speech to text and store it. Then when you ask a query, the saved text will be converted to a vector database and the most similar data to the query is retrieved.

Steps:

1. Install all the required dependencies
```
pip install -r requirements.txt
```

You will need to figure out which audio input is your Desktop Input and which is your Microphone or Headphone's input. Enabling Stereo Mix will let you listen to desktop audio when using PyAudio.

2. Go into your Control Panel > Sound > Recording tab > Enable Stereo Mix. I was using a headphone for Mic input, so depending on the audio input device, you will need to update the *input_device_index* in the *question_audio_input.py* file:
```
stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=<your suitable device index>,
                    frames_per_buffer=CHUNK)
```
All the devices can be seen using this code present in the same file:
```
p = pyaudio.PyAudio()
input_index = None
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    print("Device:",dev)
```
Next you will need to run 3 python files simultaneously in different terminals. This can also be done using multithreading.

3. Run Desktop Audio Input. It listens to your desktop audio in real time and stores it in one-minute intervals.
```
python experiments/speech/desktop_audio_input.py
```
4. Run Desktop Audio to Text. It uses Whisper to convert those audio speech files to text files.
```
python experiments/speech/desktop_audio_to_text.py
```
5. Run the HuggingFace Agent file. It uses whisper to listen to your query, then finds the relevant data and replies in audio.
```
python experiments/speech/text_reply.py
```
6. Wait till the Agent loads, then Press 'w' to start asking a question. The query listening time is hardcoded to 10 seconds.

