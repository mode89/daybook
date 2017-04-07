class Journal:

    def __init__(self):
        self.path = str()
        self.text = str()

    def load(self):
        with open(self.path, "r") as f:
            self.text = f.read()

    def append(self, entry):
        self.text += str(entry) + "\n"
