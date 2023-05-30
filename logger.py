import datetime

class Logger():
    path = "E:\\Programming\\Ever\\py\\voice_assistant\\data\\log.txt"

    def log(self, text):
        with open(self.path) as log_file:
            log_file.write(f"Time: {datetime.datetime.now()}, Text: {text}\n")