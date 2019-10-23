#!/bin/usr/python3
from Crypto.Hash import HMAC, SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto import Random
import binascii


def key_hash_genarator(key=str, salt=bytes):
    return PBKDF2(key, salt, prf=lambda p, s: HMAC.new(p, s, SHA256).digest())


def ivGenerator():
    return Random.new().read(AES.block_size)


def encryptIV(iv, hash_key):
    cipher = AES.new(hash_key, AES.MODE_ECB)
    return cipher.encrypt(iv)


def decryptIV(iv, hash_key):
    cipher = AES.new(hash_key, AES.MODE_ECB)
    return cipher.decrypt(iv)


def encrypt(text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(text)
    return ciphertext


# Gerar Hash
hash_key = key_hash_genarator('Chave Chavosa!!!', b'Slagadinho')
print("hash_key")
print(binascii.hexlify(hash_key))

# Gerar Vetor
# iv = ivGenerator()
iv = b'\x84\x18vnl:\xcfL\xa8\x8e\x8e\x7f\xc1y\xe1\xcb'
print("iv")
print(binascii.hexlify(iv))

# Encriptar IV
iv_encrp = encryptIV(iv, hash_key)
print("iv_encrp")
print(binascii.hexlify(iv_encrp))


# Decriptar IV
iv_decrp = decryptIV(iv_encrp, hash_key)
print("iv_decrp")
print(binascii.hexlify(iv_decrp))
