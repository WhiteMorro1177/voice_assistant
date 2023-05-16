import os
import subprocess

import pyttsx3 as tts
import datetime
import database

from fuzzywuzzy import process


def speak(text):
    voice_engine = tts.init()
    voice_engine.say(text)
    voice_engine.runAndWait()
    voice_engine.stop()


def execute_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak(current_time)

def execute_open(command: str):
    apps_with_paths = dict()
    apps_names = []
    for select_result in database.select_all_apps():
        apps_names.append(select_result[2])
        apps_with_paths[select_result[2]] = select_result[1]

    app_to_open = process.extractOne(command, apps_names)[0]
    speak(f"Открываю {app_to_open}")
    os.startfile(apps_with_paths[app_to_open])
    
def execute_stop():
    speak("Не могу остановиться")


class CommandExecutor():

    def execute(self, command: dict):
        if ("time" in command.keys()):
            execute_time()
        elif ("open" in command.keys()):
            print(command)
            execute_open(command["input_text"])
        elif ("stop" in command.keys()):
            execute_stop()
        else:
            speak("Не могу выполнить приказ, хозяин")
