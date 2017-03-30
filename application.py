import argparse
import datetime
import json
import os
import subprocess
import tempfile

class Application:

    def __init__(self):
        self.config_path = str()
        self.config = dict()
        self.entry = str()
        self.journal = str()
        self.args = list()

    def run(self):
        self.parse_args()
        self.config = self.load_config()
        if self.command == "entry":
            self.entry = self.compose_entry()
            if not self.entry_is_empty():
                self.load_journal()
                self.append_entry()
                self.save_journal()

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("command", nargs="?", default="entry")
        parser.parse_args(self.args, self)

    def load_config(self):
        with open(self.config_path, "r") as f:
            config = json.load(f)
        config["journal"] = os.path.expanduser(config["journal"])
        return config

    def compose_entry(self):
        with tempfile.NamedTemporaryFile("r", suffix=".txt") as f:
            subprocess.call([os.environ["EDITOR"], f.name])
            return f.read()

    def entry_is_empty(self):
        return self.entry == ""

    def load_journal(self):
        with open(self.config["journal"], "r") as f:
            self.journal = f.read()

    def append_entry(self):
        self.journal += self.time() + " " + self.entry + "\n"

    def save_journal(self):
        with open(self.config["journal"], "w") as f:
            f.write(self.journal)

    def time(self):
        timestamp = datetime.datetime.now()
        return timestamp.strftime("%Y %B %d %H:%M")
