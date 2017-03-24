import os
import subprocess
import tempfile

class Application:

    def run(self):
        self.edit()

    def edit(self):
        with tempfile.NamedTemporaryFile("r", suffix=".txt") as f:
            subprocess.call([os.environ["EDITOR"], f.name])
            return f.read()
