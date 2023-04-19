from fuzzywuzzy import process
import database
import os

# rewrite with database

'''
In "process":

first arg - string with recognized voice
second arg - collection with choices

'''


input_command = "бот скажи сколько сейчас время"  # распознанная фраза

select_options_result = database.select_all_options()
commands = []
aliases = []

for cmd in database.select_option("cmd"):
    commands.append(cmd[1])

print(commands)


for alias in database.select_option("alias"):
    aliases.append(alias[1])

print(aliases, "\n")

# ------------------------------------

process_result_aliases = process.extract(input_command, aliases)
process_result_commands = process.extract(input_command, commands)

print(process_result_aliases)
print(process_result_commands)


'''
cfg = config.options
phrase_extraction = dict()

for option in config.options:
    phrase_extraction[option] = process.extractOne(cmd, cfg[option])


final_cmd = process.extractOne(cmd, phrase_extraction["cmd"][0])
if (final_cmd[1] > 50):
    if (final_cmd[0] in cfg["cmd"]["time"]):
        print("Time: ")
        #  TODO(Show system time)


'''