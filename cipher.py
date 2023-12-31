import base64
import hashlib
import pickle
from Crypto import Random
from Crypto.Cipher import AES


FNAME = "data"

class AESCipher(object):

    def __init__(self, key: str):
        key = f"gg_{key}ff__"
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, ct: str) -> bytes:
        ct = self._pad(ct)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(ct.encode()))

    def decrypt(self, enc) -> str:
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return AESCipher._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    @staticmethod
    def save(dlist: list[dict]):
        with open(FNAME, 'wb') as f:
            pickle.dump(dlist, f)

    def load(self) -> list[dict]:
        with open(FNAME, 'rb') as f:
            try:
                return pickle.load(f)
            except:
                return []