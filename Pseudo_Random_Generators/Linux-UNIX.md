# Geração de Números Pseudoaleatórios no Linux e derivados de UNIX.

Dentro das pesquisas realizadas nas bibliotecas *Python*, **[secrets](https://docs.python.org/3/library/secrets.html)**, **[Crypto](https://pycryptodome.readthedocs.io/en/latest/src/random/random.html)** e **[cryptography](https://cryptography.io/en/latest/random-numbers/)**. Todas utilizam os geradores nativos dos sistemas onde operam. No caso do Linux e derivados de UNIX, o *pool* para geração dos PRNs são:

O **```/dev/random```**, que tem uso variado e pode ser considerado o *pool* supremo, para se utilizar com PRNGs, em sistemas UNIX. Possui bloqueio para liberar os dados apenas quando consegue entropia suficiente para gerar encriptação da ordem de 4096 bits ou mais.

O **```/dev/urandom```** pode ser utilizado para diversos fins, exeto para segurança. Pois não possui um sistema de travamento para o caso de não atingir uma qunatidade suficiente de números entrópicos.

## Entropia
As principais fontes de entropia do kernel, para alimentar as *pools* do sistema são:
- Teclado
- Disco
- Mouse

Além de muitas outras como a rede e dumps/espaços de memória.

*No caso de máquinas como servidores, onde não há interação humana, as pools serão preenchidas de forma mais vagarosa. Haja vista, que o 1º e 3º elemento não estão disponíveis.*

Referência: [RFC-4086](https://tools.ietf.org/html/rfc4086#section-7.1.2)

## Conclusão
De forma geral nos sistemas UNIX, para geração de números pseudoaleatórios, o PRNG busca sua semente nas *pools* já mencionadas e com base no algoritmo gera o PRN.