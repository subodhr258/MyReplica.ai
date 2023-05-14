import pyttsx3

def run_speak_reply(reply):
        
    # Initialize the engine
    engine = pyttsx3.init()

    # Set the voice properties (change as needed)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.7)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(reply)
    engine.runAndWait()