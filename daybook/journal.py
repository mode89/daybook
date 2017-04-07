class Journal:

    def __init__(self):
        self.path = str()
        self.text = str()

    def load(self):
        with open(self.path, "r") as f:
            self.text = f.read()

    def save(self):
        with open(self.path, "w") as f:
            f.write(self.text)

    def append(self, entry):
        self.text += str(entry) + "\n"
