import daybook.cipher

class Journal:

    def __init__(self):
        self.path = str()
        self.text = str()
        self.data = bytes()

    def load(self):
        with open(self.path, "rb") as f:
            self.data = f.read()

    def save(self):
        with open(self.path, "wb") as f:
            f.write(self.data)

    def decode(self):
        self.text = self.data.decode("utf-8")

    def encode(self):
        self.data = self.text.encode("utf-8")

    def append(self, entry):
        self.text += str(entry) + "\n"

    def encrypt(self):
        cipher = daybook.cipher.Cipher(self.password)
        self.data = cipher.encrypt(self.data)

    def decrypt(self):
        cipher = daybook.cipher.Cipher(self.password)
        self.data = cipher.decrypt(self.data)
