from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import os

files = os.listdir("D:\\Programs\\py\\voice_assistant\\")

a = process.extractOne("cofg.py", files)
'''
In "process":

first arg - string with recognized voice
second arg - collection with choices

'''
print(a)

