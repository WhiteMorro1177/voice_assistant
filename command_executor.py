import pyttsx3 as tts
import datetime

from recognizer import Recognizer
from fuzzywuzzy import process

'''
from recognizer: 

{ 
    'cmd': ( {
            'cmd_name': {
                'открой', 
                'запусти'
                }, 
            'app': {
                'браузер': 'firefox.exe', 
                'файлы': 'explorer.exe',
                }
            }, 
            86, 
            'open'
        ), 
    'start_command': 'григорий открой браузер'
}

output format: 
"cmd" :
    [0] - tuple of commands
    [1] - equality value
    [2] - command name

"start_command":
    [0] - start command
'''

def speak(text):
    voice_engine = tts.init()
    voice_engine.say(text)
    voice_engine.runAndWait()
    voice_engine.stop()


def execute_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    print(current_time)

def execute_open(command: dict):
    start_command = command["start_command"]
    apps = command["cmd"][0]["app"]
    
    app_to_open = process.extractOne(start_command, apps)
    print(app_to_open)
    


class CommandExecutor():

    def execute(self, command: dict):
        command_name = command["cmd"]
        print(command_name)
        if ("time" in command_name):
            execute_time()
        elif ("open" in command_name):
            execute_open(command)
        else:
            print("Nothing to execute")
