import os
import subprocess
import tempfile

def main():
    compose_text()

def compose_text():
    with tempfile.NamedTemporaryFile("r", suffix=".txt") as f:
        subprocess.call([os.environ["EDITOR"], f.name])
        return f.read()

if __name__ == "__main__":
    main()
