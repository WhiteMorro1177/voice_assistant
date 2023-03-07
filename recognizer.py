from config import options
from fuzzywuzzy import process

class Recognizer():

    # TODO(upgrade Recognizer (if needed))
    # recognized text goes with bot name
    def recognize(self, recognized_text):
        phrase_extraction = dict()

        for option in options:
            phrase_extraction[option] = process.extractOne(recognized_text, options[option])

        final_cmd = process.extractOne(recognized_text, phrase_extraction["cmd"][0])
        if (final_cmd[1] > 50):
            return final_cmd[0]