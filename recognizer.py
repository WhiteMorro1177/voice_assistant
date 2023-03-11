from config import options
from fuzzywuzzy import process

class Recognizer():

    def recognize(self, recognized_text, tag) -> dict:
        phrase_extraction = dict()

        for option in options:
            phrase_extraction[option] = process.extractOne(recognized_text, options[option])

        result = dict()
        result[tag] = phrase_extraction[tag]
        result["start_command"] = recognized_text
        return result
    
    '''
        output format: 
            [0] - tuple of commands
            [1] - equality value
            [2] - command name
            [3] - start command
    '''