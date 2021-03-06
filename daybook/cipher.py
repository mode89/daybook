import Crypto.Cipher.AES
import Crypto.Hash.SHA256
import Crypto.Random

class Cipher:

    def __init__(self, password):
        self.block_size = 16
        self.generate_key(password)

    def generate_key(self, password):
        h = Crypto.Hash.SHA256.new()
        h.update(password.encode("utf-8"))
        self.key = h.digest()

    def add_padding(self, data):
        padding_length = self.block_size - len(data) % self.block_size
        padding = b'\x00' * padding_length
        return data + padding

    def remove_padding(self, data):
        return data.rstrip(b'\x00')

    def encrypt(self, data):
        data = self.add_padding(data)
        Crypto.Random.atfork()
        aes = Crypto.Cipher.AES
        init_vector = Crypto.Random.new().read(self.block_size)
        # force first byte to be undecodable by decode("utf-8")
        # which can be used to differentiate encrypted and plain text
        init_vector = b'\xFF' + init_vector[1:]
        cipher = aes.new(self.key, aes.MODE_CBC, init_vector)
        return init_vector + cipher.encrypt(data)

    def decrypt(self, data):
        aes = Crypto.Cipher.AES
        init_vector = data[:self.block_size]
        data = data[self.block_size:]
        cipher = aes.new(self.key, aes.MODE_CBC, init_vector)
        data = cipher.decrypt(data)
        return self.remove_padding(data)
