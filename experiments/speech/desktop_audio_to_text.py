import whisper
import os
import time

folder_path = './saved_audio'  # The path to the folder containing the output files
model = whisper.load_model("small")

while True:
    # Sleep for 10 seconds
    time.sleep(10)
    print("Detecting audio files...")
    # Check if there are any audio files in the folder
    audio_files = [f for f in os.listdir(folder_path) if f.startswith('output') and f.endswith('.wav')]
    for audio_file in audio_files:
        audio_file = os.path.join(folder_path, audio_file)
        audio = whisper.load_audio(audio_file)
        audio = whisper.pad_or_trim(audio)

        mel = whisper.log_mel_spectrogram(audio).to(model.device)

        options = whisper.DecodingOptions(fp16 = False)
        result = whisper.decode(model, mel, options)

        print(audio_file, ":", result.text)
        with open("./saved_text/text.txt", "a") as file:
            file.write(f"\n{result.text}")
        os.remove(audio_file)