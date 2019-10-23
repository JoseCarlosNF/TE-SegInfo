from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import Salsa20
from Crypto.Hash import SHA512
from os import urandom
import binascii

"""
    Algoritmo:
        Salsa20

    Descrição:
        - Baseado em operações de XOR e rotação.
        - Mapeia uma chave de 256-bits.
        - Utiliza um Nonce de 64-bits.

    Considerações:
        De forma padrão o Salsa20 não garante a integridade da informação, apenas sua confidencialidade.
        Para sobrepor isso utiliza-se uma MAC (Message Authentication Code).
"""


class Salsa20_StreamCipher():
    def __init__(self, text=bytes, key=bytes):
        self.text = text
        self.key = key

    def __DeriveKey(self, password):
        salt = get_random_bytes(16)
        key_derivate = PBKDF2(password, salt, 16,
                              count=100000, hmac_hash_module=SHA512)
        return key_derivate

    def encrypt(self):
        key_derivate = self.__DeriveKey(self.key)
        cipher = Salsa20.new(key_derivate, nonce=urandom(8))
        return cipher.nonce + cipher.encrypt(self.text), key_derivate

    def decrypt(self):
        nonce = self.text[:8]
        ciphertext = self.text[8:]
        cipher = Salsa20.new(key=self.key, nonce=nonce)
        return cipher.decrypt(ciphertext)


if __name__ == "__main__":
    print("Welcome to \033[0;1mSalsa20\033[0m Stream Cipher Demonstration 😄")

    option = int(input("🔐 1-Cipher | 🔓 2-Decipher\n>>>"))

    if (option == 1):
        enter_key = bytes(input("🔑  : "), 'utf-8')
        enter_text = bytes(input("🔤  : "), 'utf-8')

        cipher = Salsa20_StreamCipher(text=enter_text, key=enter_key)
        text_encrp, key_derivate = cipher.encrypt()

        print("\033[0;1mUse to Decipher\033[0m")
        print("🔐  : %s" % binascii.hexlify(text_encrp))
        print("🔑  : %s" % binascii.hexlify(key_derivate))

    elif (option == 2):
        print("Isert X characters b'\033[0;1mXXXXXXXXXXXXXXXX\033[0m'")
        enter_key = bytes(input("🔑  : "), 'utf-8')
        enter_text = bytes(input("🔐  : "), 'utf-8')

        enter_key = binascii.unhexlify(enter_key)
        enter_text = binascii.unhexlify(enter_text)

        cipher = Salsa20_StreamCipher(text=enter_text, key=enter_key)
        text_decrp = cipher.decrypt()

        print("\033[0;1m Texto Plano\033[0m : %s" % str(text_decrp))
