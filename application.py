import json
import os
import subprocess
import tempfile

class Application:

    def __init__(self):
        self.config = dict()
        self.journal = str()

    def load_config(self, file_name):
        with open(file_name, "r") as f:
            self.config = json.load(f)

    def run(self):
        text = self.edit()
        # do not add empty records
        if text != "":
            self.journal += self.time() + " " + text
            # save journal
            with open(self.config["journal"], "w") as f:
                f.write(self.journal)

    def edit(self):
        with tempfile.NamedTemporaryFile("r", suffix=".txt") as f:
            subprocess.call([os.environ["EDITOR"], f.name])
            return f.read()

    def time(self):
        return str()
