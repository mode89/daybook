import datetime
import json
import os
import subprocess
import tempfile

class Application:

    def __init__(self):
        self.config_path = os.path.expanduser("~/.journal")
        self.config = dict()
        self.record = str()
        self.journal = str()

    def run(self):
        self.config = self.load_config()
        self.record = self.compose_record()
        if not self.record_is_empty():
            self.load_journal()
            self.append_record()
            self.save_journal()

    def load_config(self):
        with open(self.config_path, "r") as f:
            config = json.load(f)
        config["journal"] = os.path.expanduser(config["journal"])
        return config

    def compose_record(self):
        with tempfile.NamedTemporaryFile("r", suffix=".txt") as f:
            subprocess.call([os.environ["EDITOR"], f.name])
            return f.read()

    def record_is_empty(self):
        return self.record == ""

    def load_journal(self):
        with open(self.config["journal"], "r") as f:
            self.journal = f.read()

    def append_record(self):
        self.journal += self.time() + " " + self.record + "\n"

    def save_journal(self):
        with open(self.config["journal"], "w") as f:
            f.write(self.journal)

    def time(self):
        timestamp = datetime.datetime.now()
        return timestamp.strftime("%Y %B %d %H:%M")
