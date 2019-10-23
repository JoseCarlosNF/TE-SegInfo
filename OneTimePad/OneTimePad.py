#!/usr/bin/python3

from os import system
from secrets import randbelow
""" [secrets] utiliza [os.urandom] para acessar geradores do sistema."""


class OneTimePad:

    def __init__(self, text=str):
        self.text = text.upper()
        self.Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

    def getLetterIndex(self, letter=str):
        return self.Alphabet.index(letter)

    def generateKey(self):
        key = str()
        for char in self.text:
            letter_index = randbelow(26)
            key += self.Alphabet[letter_index]
        return key

    def cipher(self):
        ciphertext = str()
        key = self.generateKey()

        for i in range(len(self.text)):
            plain_index = self.getLetterIndex(self.text[i])
            key_index = self.getLetterIndex(key[i])
            ciphertext += self.Alphabet[(plain_index + key_index) % 27]
        return key, ciphertext

    def decipher(self, key=str):
        deciphered_text = str()
        key = key.upper()

        for i in range(len(self.text)):
            cipher_index = self.getLetterIndex(self.text[i])
            key_index = self.getLetterIndex(key[i])
            deciphered_text += self.Alphabet[(cipher_index - key_index) % 27]
        return deciphered_text

    def generateKey_byCiphertext(self, Ciphertext=str):
        """ Plain text and ciphertext required """
        Ciphertext = Ciphertext.upper()
        key = ''

        for i in range(len(Ciphertext)):
            cipher_index = self.getLetterIndex(Ciphertext[i])
            plain_index = self.getLetterIndex(self.text[i]) 
            key += self.Alphabet[(cipher_index - plain_index) % 27]
        return key



if __name__ == "__main__":
    system("clear")
    while True:
        print("One-time Pad Demonstration!!😃 ")
        operation = int(input("🔐 1-Cipher | 🔓 2-Decipher | 🔑 3-Get Key |🚪 0-Exit \n>>>"))

        if operation == 1:
            text = OneTimePad(input("🔓 : "))
            key, ciphertext = text.cipher()
            print("🔑 : " + key)
            print("🔐 : " + ciphertext)
            input()

        elif operation == 2:
            text = OneTimePad(input("🔐 : "))
            key = input("🔑 : ")
            print("🔓 : " + text.decipher(key))
            input()

        elif operation == 3:
            text = OneTimePad(input("🔓 : "))
            ciphertext = input("🔐 : ")
            print("🔑 : " + text.generateKey_byCiphertext(ciphertext))
            input()

        elif operation == 0:
            print("👋")
            break
        system("clear")
