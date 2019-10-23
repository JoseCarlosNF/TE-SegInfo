#!/usr/bin/python3
""" Implementação de um Gerador de Números Pseudoaleatórios """

from secrets import SystemRandom
import random

"""
    # secrets:
        Generate cryptographically strong pseudo-random numbers suitable for
        managing secrets such as account authentication, tokens, and similar.

    # secrets.SystemRandom:
        Alternate random number generator using sources provided
        by the operating system (such as /dev/urandom on Unix or
        CryptGenRandom on Windows).
        Not available on all systems (see os.urandom() for details).

    ! Considerações:
        Como pode-se notar, a biblioteca utiliza como pool de entropia as fontes fornecidas pelo sistema.
        -   /dev/urandom :: Unix
        - CryptGenRandom :: MS-Windows
"""

# 🚨 Gerador randomico SEGURO
generator = SystemRandom()
print(generator.getrandbits(1024)) # Gera um inteiro de 1024-bits
print(generator.random())

# 🕹 Gerador randomico USUAL do Python
print(random.random())

""" 
! Conclusão:
    Seguindo as documentações, ambos os geradores utilizam a mesma fonte de entropia.

    ? Podemos então afirmar que o PRNG built-in do Python é seguro?
"""
