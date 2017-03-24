import os
import subprocess
import tempfile

if __name__ == "__main__":
    with tempfile.NamedTemporaryFile("r", suffix=".txt") as f:
        subprocess.call([os.environ["EDITOR"], f.name])
        print(f.read())
