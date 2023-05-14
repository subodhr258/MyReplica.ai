import whisper

# Select from the following models: "tiny", "base", "small", "medium", "large"
model = whisper.load_model("tiny")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("/saved_audio/audio.wav")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# decode the audio
options = whisper.DecodingOptions(fp16 = False)
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)