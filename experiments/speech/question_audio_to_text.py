import whisper
import os
import time

folder_path = './saved_audio'  # The path to the folder containing the output files
model = whisper.load_model("small")

def ques_speech_to_text():
    print("Converting question audio to text...")
    folder_path = "./"
    audio_files = [f for f in os.listdir(folder_path) if f.startswith('question') and f.endswith('.wav')]
    audio_file = audio_files[0]
    audio_file = os.path.join(folder_path, audio_file)
    audio = whisper.load_audio(audio_file)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)
    print(audio_file, ":", result.text)
    # os.remove(audio_file)
    
    return result.text