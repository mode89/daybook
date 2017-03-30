import application
import os
import sys

if __name__ == "__main__":
    app = application.Application()
    app.config_path = os.path.expanduser("~/.journal")
    app.args = sys.argv[1:]
    app.run()
