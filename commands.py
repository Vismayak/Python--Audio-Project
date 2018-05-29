import subprocess
import os


class Commands:

    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "do not", "cancel"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            self.respond("My name is python. How are you?")
        if "are" in text and "you" and "kill me" in text:
            self.respond("Not now but soon")
        if text.startswith("open"):
            app = text.split(" ",1)[1]
            # print(app)
            # print("here")
            self.respond("Opening " + app)
            os.system("open -a " + app)

    def respond(self, text):
        print(text)
        subprocess.call('say -v "Victoria" '+ text, shell=True)
