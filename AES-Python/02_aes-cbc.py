import binascii
from Crypto.Cipher import AES
from Crypto import Random

"""
    📑 AES em modo CBC

    🔖 Decricao:
        Um dos modos seguros de criptografar dados.
        - Tem um esquema de rodadas, onde a entrada de um bloco, depende da saida do anterior.
        - Pode ser usado para cifrar quantidades maiores de dados.
        - Remove as caracteristicas do texto plano, como frequencia e repeticao.
        - A sua saida em nada tem haver com sua entrada plana.
        - O mesmo texto pode ser criptografado varias vezes e tera resultados divergentes.

    🌟 Peculiaridades:
        - E obrigatorio o uso de um IV (Initialization Vector)
        - Nao pode ser paralelizado.
        - A mensagem deve ser preenchida [padding], para ter um tamanho multiplo do tamanho do bloco da cifra.
        
"""


class AES_CBC():
    def __init__(self, text, key, iv):
        self.key = key
        self.iv = iv
        self.text = text

    def encrypt(self):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.encrypt(self.text)

    def decrypt(self):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.decrypt(self.text)


if __name__ == '__main__':
    # 👨‍🍳 Definicao de CHAVE e TEXTO PLANO
    txt = 'texto plano blz!'
    key = 'chave chavosa!!!'

    # 🏁 Vetor de inicializacao
    # E de suma importancia que o vetor de inicializacao seja gerado de forma aleatoria.
    # No caso em questao, foi utilizada o gerador da propria biblioteca para gerar o IV.
    iv = Random.new().read(AES.block_size)

    # 🧱 Instanciando objeto AES_CBC, com TEXTO PLANO
    texto = AES_CBC(txt, key, iv)

    # 🔐 Crifragem
    texto_cifrado = texto.encrypt()

    # 🧱 Instanciando objeto AES_CBC, com TEXTO CIFRADO
    texto = AES_CBC(texto_cifrado, key, iv)

    # 🔓 Decifragem
    texto_decifrado = texto.decrypt()

    # 👀 Apresentacoes
    print('\033[33;1mVetor de Inicializacao:')
    print('\033[0;1m %s' % binascii.hexlify(iv))

    print('\033[31;1mTexto Cifrado:')
    print('\033[0;1m %s' % binascii.hexlify(texto_cifrado))

    print('\033[32;1mTexto Decifrado:')
    print('\033[0;1m %s' % texto_decifrado)
