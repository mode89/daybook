import os
import subprocess
import tempfile

class Application:

    def __init__(self):
        self.journal = str()

    def run(self):
        self.journal += self.time() + " " + self.edit()

    def edit(self):
        with tempfile.NamedTemporaryFile("r", suffix=".txt") as f:
            subprocess.call([os.environ["EDITOR"], f.name])
            return f.read()

    def time(self):
        return str()
