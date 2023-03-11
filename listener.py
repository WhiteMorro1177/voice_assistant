import speech_recognition as sr

from recognizer import Recognizer
from command_executor import CommandExecutor
import config
import time

ALIAS_TAG = "alias"
COMMAND_TAG = "cmd"
APPLICATION_TAG = "app"

class Listener():

    def listen(self):
        speech_recognizer = sr.Recognizer()
        microphone = sr.Microphone(config.microphone_index)

        with microphone as source:
            speech_recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Listening...")

        background = speech_recognizer.listen_in_background(microphone, callback)
        while True: time.sleep(0.1)


def callback(speech_recognizer: sr.Recognizer, source: sr.Microphone):
    try:
        voice_to_text = speech_recognizer.recognize_google(source, language="ru-RU")
        print("Распознано" + voice_to_text)

        command_recognizer = Recognizer()
        executor = CommandExecutor()

        if (command_recognizer.recognize(voice_to_text, ALIAS_TAG)[1] > 70):
            command = command_recognizer.recognize(voice_to_text, COMMAND_TAG)
            executor.execute(command)

    except:
        print("Не распознано")
