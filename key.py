import hmac
import hashlib
import os


class HmacSha3Generator:
    def __init__(self):
        self.key = os.urandom(32)

    def generatehmac(self, number: int) -> str:
        numberbytes = str(number).encode('utf-8')
        hmacobj = hmac.new(self.key, numberbytes, hashlib.sha3_256)
        return hmacobj.hexdigest().upper()

    def getKey(self) -> str:
        return self.key.hex().upper()

    def verifyhmac(self, number: int, rechmac: str) -> bool:
        numberbytes = str(number).encode('utf-8')
        new_hmac = hmac.new(self.key, numberbytes, hashlib.sha3_256).hexdigest().upper()
        return hmac.compare_digest(new_hmac, rechmac)
