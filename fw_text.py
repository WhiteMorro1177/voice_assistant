from fuzzywuzzy import process
import config
import os

files = os.listdir("D:\\Programs\\py\\voice_assistant\\")

a = process.extractOne("cofg.py", files)
'''
In "process":

first arg - string with recognized voice
second arg - collection with choices

'''
# print(a)

cmd = "григорий скажи сколько сейчас время"  # распознанная фраза

cfg = config.options
phrase_extraction = dict()

for option in config.options:
    phrase_extraction[option] = process.extractOne(cmd, cfg[option])


final_cmd = process.extractOne(cmd, phrase_extraction["cmd"][0])
if (final_cmd[1] > 50):
    if (final_cmd[0] in cfg["cmd"]["time"]):
        print("Time: ")
        #  TODO(Show system time)


