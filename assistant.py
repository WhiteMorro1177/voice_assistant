import speech_recognition as sr
import pyttsx3 as tts
import datetime
import config
import time
import os


def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(config.microphone_index)

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")

    background = recognizer.listen_in_background(microphone, callback)
    while True: time.sleep(0.1)


def speak(text):
    voice_engine = tts.init()
    voice_engine.say(text)
    voice_engine.runAndWait()
    voice_engine.stop()


def callback(recognizer: sr.Recognizer, source: sr.Microphone):
    try:
        voice_to_text = recognizer.recognize_google(source, language="ru-RU")
        print("Распознано" + voice_to_text)

        if voice_to_text.startwith(config.options["alias"]):
            command = voice_to_text.remove(config.options["alias"])
            command = voice_to_text.remove(config.options["tbr"])

            #  cmd = recognize_command(command)
            #  execute_command(cmd)
    except:
        print("Не распознано")


def recognize_command(cmd):


    pass

def execute_command(cmd):
    # TODO(think about type)
    pass




if __name__ == "__main__": main()
