from Crypto.Cipher import AES
from binascii import unhexlify, hexlify
import binascii

"""
    📑 AES em modo ECB

    🔖 Decricao:
        - O modo ECB (electronic codebook) e o modo mais simples de encriptacao, dentre todos os modos de oparacao criptograficos.
        - Funciona  com encriptacao por blocos.


    🌟 Peculiaridades:
        - Nao e necessario IV (Initialization Vector);
        - Nao e recomendado, para encriptar grandes quantidades de dados
        - 
"""

class AES_ECB():
    def __init__(self, text=str, key=str):
        self.text = text
        self.key = key

    def encrypt(self):
        cipher = AES.new(self.key, AES.MODE_ECB)
        return cipher.encrypt(self.text)

    def decrypt(self):
        cipher = AES.new(self.key, AES.MODE_ECB)
        return cipher.decrypt(self.text)

if __name__ == '__main__':
    # 👨‍🍳 Definicao de CHAVE e TEXTO PLANO
    txt = 'texto plano blz!texto plano blz!'
    key = 'chave chavosa!!!chave chavosa!!!'

    # 🧱 Instaciar objeto da classe AES_ECB, com o TEXTO PLANO e a CHAVE
    plaintext = AES_ECB(txt, key) 

    # 🔐 Criptografar
    texto_cifrado = plaintext.encrypt()

    # 🧱 Instaciar objeto da classe AES_ECB, com o TEXTO PLANO e a CHAVE
    ciphertext = AES_ECB(texto_cifrado, key)

    # 🔓 Decriptografar
    texto_decifrado = ciphertext.decrypt()    

    # 👀 Apresentacoes
    # O texto cifrado gerado tem formato bytes, [b'exmplo'], em hexadecimal
    # podemos converte-lo para hexadecimal ascii.
    print('\033[31;1mTexto Cifrado:')
    print('\033[0;1m %s' % binascii.hexlify(texto_cifrado))

    print('\033[32;1mTexto Decifrado:')
    print('\033[0;1m %s' % texto_decifrado)