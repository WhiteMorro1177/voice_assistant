import pyttsx3 as tts

def speak(text):
    voice_engine = tts.init()
    voice_engine.say(text)
    voice_engine.runAndWait()
    voice_engine.stop()