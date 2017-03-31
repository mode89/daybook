import argparse
import daybook.cipher
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
        self.execute_command()

    def execute_command(self):
        attr = "command_" + self.command
        if hasattr(self, attr):
            getattr(self, attr)()
        else:
            raise RuntimeError("Unknown command: {0}".format(self.command))

    def command_entry(self):
        self.entry = self.compose_entry()
        if not self.entry_is_empty():
            self.load_journal()
            self.append_entry()
            self.save_journal()

    def command_edit(self):
        self.load_journal()
        self.journal = self.edit_text(self.journal)
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

    def edit_text(self, text):
        fd, path = tempfile.mkstemp()
        try:
            os.write(fd, text.encode("utf-8"))
            os.close(fd)
            subprocess.call([os.environ["EDITOR"], path])
            with open(path, "r") as f:
                return f.read()
        finally:
            os.remove(path)

    def compose_entry(self):
        return self.edit_text("")

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

    def encrypt_journal(self):
        cipher = daybook.cipher.Cipher(self.password)
        self.journal = cipher.encrypt(self.journal.encode("utf-8"))

    def time(self):
        timestamp = datetime.datetime.now()
        return timestamp.strftime("%Y %B %d %H:%M")
