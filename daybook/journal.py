class Journal:

    def __init__(self):
        self.text = str()

    def append(self, entry):
        self.text += str(entry) + "\n"
