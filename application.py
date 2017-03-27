import json
import os
import subprocess
import tempfile

class Application:

    def __init__(self):
        self.config_path = "~/.journal"
        self.config = dict()
        self.record = str()
        self.journal = str()

    def run(self):
        self.config = self.load_config()
        self.record = self.compose_record()
        if not self.record_is_empty():
            self.append_record()
            self.save_journal()

    def load_config(self):
        with open(self.config_path, "r") as f:
            return json.load(f)

    def compose_record(self):
        with tempfile.NamedTemporaryFile("r", suffix=".txt") as f:
            subprocess.call([os.environ["EDITOR"], f.name])
            return f.read()

    def record_is_empty(self):
        return self.record == ""

    def append_record(self):
        self.journal += self.time() + " " + self.record

    def save_journal(self):
        with open(self.config["journal"], "w") as f:
            f.write(self.journal)

    def time(self):
        return str()
