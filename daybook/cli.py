from . import application
import os
import sys

def main():
    app = application.Application()
    app.config_path = os.path.expanduser("~/.daybook")
    app.args = sys.argv[1:]
    app.run()

if __name__ == "__main__":
    main()
