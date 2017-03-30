import application
import os

if __name__ == "__main__":
    app = application.Application()
    app.config_path = os.path.expanduser("~/.journal")
    app.run()
