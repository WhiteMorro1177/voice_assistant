import speech_recognition as sr

from speaker import *
from recognizer import *
import time

class Listener():

    def listen(self):
        speech_recognizer = sr.Recognizer()
        microphone = sr.Microphone(1)

        with microphone as source:
            speech_recognizer.adjust_for_ambient_noise(source, duration=2)
            speak("Слушаю, мастер")

        background = speech_recognizer.listen_in_background(microphone, callback)
        while True: time.sleep(0.1)


def callback(speech_recognizer: sr.Recognizer, source: sr.Microphone):
    try:
        voice_to_text = speech_recognizer.recognize_google(source, language="ru-RU")
        print("Распознано: " + voice_to_text)

        r = Recognizer()
        if (r.recognize(voice_to_text, "alias")):
            r.recognize(voice_to_text, "cmd")

    except:
        print("Не распознано")
