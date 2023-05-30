import os
import webbrowser

from speaker import *
import datetime
import database

from fuzzywuzzy import process


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

def execute_find(request: str):
    request = request.lower()
    to_be_remove = []
    for select_result in database.select_all_options():
        '''
            select_result[0] - id
            select_result[1] - name
            select_result[2] - option tag
            select_result[3] - command type tag
        '''

        if ("alias" == select_result[2]):
            to_be_remove.append(select_result[1])
        if ("browse" == select_result[3]):
            to_be_remove.append(select_result[1])

    for cmd in to_be_remove:
        if (cmd in request):
            request = request.replace(cmd, "")

    webbrowser.open_new_tab(f"https://www.google.com/search?q={request.strip().replace(' ', '+')}")

def execute_stop():
    speak("Всего хорошего, мастер")


class CommandExecutor():

    def execute(self, command: dict):
        if ("time" in command.keys()):
            execute_time()
        elif ("open" in command.keys()):
            execute_open(command["input_text"])
        elif ("browse" in command.keys()):
            execute_find(command["input_text"])
        elif ("stop" in command.keys()):
            execute_stop()
        else:
            speak("Не могу выполнить приказ, хозяин")
