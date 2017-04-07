import daybook.cipher

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

    def encrypt(self):
        cipher = daybook.cipher.Cipher(self.password)
        self.text = cipher.encrypt(self.text.encode("utf-8"))

    def decrypt(self):
        cipher = daybook.cipher.Cipher(self.password)
        self.text = cipher.decrypt(self.text).decode("utf-8")
