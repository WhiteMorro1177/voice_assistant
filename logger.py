import os

class Logger():
    path = "log.txt"

    def log(self, text): # without endline
        with open(self.path) as log_file:
            log_file.write(text + "\n")