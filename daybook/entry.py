import datetime

class Entry:

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.time() + " " + self.text

    def is_empty(self):
        return self.text == ""

    def time(self):
        timestamp = datetime.datetime.now()
        return timestamp.strftime("%Y %B %d %H:%M")
