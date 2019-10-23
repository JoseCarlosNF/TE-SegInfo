#!/usr/bin/python3
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256, HMAC
from Crypto.Cipher import AES
from Crypto import Random
import binascii


class AES_CBC_PBKDF2():
    def __init__(self, text, key=str, salt=bytes):
        self.text = text
        self.salt = salt
        self.key = key

    def __ivGenerator(self):
        return Random.new().read(AES.block_size)

    def __key_hash_genarator(self):
        return PBKDF2(self.key, self.salt, prf=lambda p, s: HMAC.new(p, s, SHA256).digest())

    def __encryptIV(self, iv):
        cipher = AES.new(self.__key_hash_genarator(), AES.MODE_ECB)
        return cipher.encrypt(iv)

    def __decryptIV(self, iv):
        cipher = AES.new(self.__key_hash_genarator(), AES.MODE_ECB)
        return cipher.decrypt(iv)

    def encrypt(self):
        iv = self.__ivGenerator()
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(self.text)
        iv_ecrypted = self.__encryptIV(iv)
        return ciphertext, iv_ecrypted

    def decrypt(self, iv_encrypted):
        iv = self.__decryptIV(iv_encrypted)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.decrypt(self.text)


# TODO: Fazer preenchimento de TEXTOS e CHAVES maiores e menores que 16,24, 32 bytes.
# TODO: Quebrar os blocos de tamanhos maiores que 32 bytes, exemplo arquivos de texto.
if __name__ == "__main__":
    print(
        "Welcome to \033[0;1mAES-CBC \033[0mwith \033[0;1mPBKDF2 \033[0mfor IV trasnmission 🤙")
    option = int(input("🔐 1-Cipher | 🔓 2-Decipher | 🚪 0-Exit\n>>>"))

    if option == 0:
        exit('👋')

    key = input('Enter 🔑 : ')
    salt = bytes(input('Salt 🧂 : '), 'utf-8')

    # 🔒 Cipher 
    if option == 1:
        # 🔤 Entries
        plaintext = input('Plaintext 🔤 : ')

        # 🧙 The magic is make here
        cipher = AES_CBC_PBKDF2(plaintext, key, salt)
        ciphetext_IVencrypted = cipher.encrypt()

        # 👀 Presentation
        print('\033[31;1mCiphertext:\033[0;1m')
        print(binascii.hexlify(ciphetext_IVencrypted[0]))

        print('\033[31;1mIV Encrypted:\033[0;1m')
        print(binascii.hexlify(ciphetext_IVencrypted[1]))

    # 🔓 Decipher
    elif option == 2:
        # 🔤 Entries
        ciphertext = binascii.unhexlify(
            bytes(input('Ciphertext 🔐 : '), 'utf-8'))
        iv_encrypted = binascii.unhexlify(
            bytes(input('IV Encrypted 🚩 : '), 'utf-8'))

        # 🧙 The magic is make here
        cipher = AES_CBC_PBKDF2(ciphertext, key, salt)
        plaintext = cipher.decrypt(iv_encrypted)

        # 👀 Presentation
        print('\033[32;1mPlain text:\033[0;1m')
        print(binascii.hexlify(plaintext))
