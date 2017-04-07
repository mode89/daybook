import argparse
import daybook.cipher
import daybook.entry
import daybook.journal
import datetime
import getpass
import json
import os
import subprocess
import tempfile

class Application:

    def __init__(self):
        self.config_path = str()
        self.config = dict()
        self.journal = daybook.journal.Journal()
        self.args = list()

    def run(self):
        self.parse_args()
        self.config = self.load_config()
        self.journal.path = self.config["journal"]
        self.execute_command(self.command)

    def execute_command(self, command):
        attr = "command_" + command
        if hasattr(self, attr):
            getattr(self, attr)()
        else:
            raise RuntimeError("Unknown command: {0}".format(command))

    def command_entry(self):
        self.entry = self.compose_entry()
        if not self.entry.is_empty():
            self.journal.load()
            self.journal.append(self.entry)
            self.journal.save()

    def command_encrypt(self):
        self.password = self.enter_password()
        self.journal.load()
        self.encrypt_journal()
        self.journal.save()

    def command_edit(self):
        self.journal.load()
        self.journal.text = self.edit_text(self.journal.text)
        self.journal.save()

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
        text = self.edit_text("")
        return daybook.entry.Entry(text)

    def enter_password(self):
        password = getpass.getpass(prompt="Password: ")
        repeat_password = getpass.getpass(prompt="Repeat password: ")
        assert password == repeat_password
        return password

    def encrypt_journal(self):
        cipher = daybook.cipher.Cipher(self.password)
        self.journal.text = \
            cipher.encrypt(self.journal.text.encode("utf-8"))

    def decrypt_journal(self):
        cipher = daybook.cipher.Cipher(self.password)
        self.journal.text = \
            cipher.decrypt(self.journal.text).decode("utf-8")
