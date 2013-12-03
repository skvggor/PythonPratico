"""
Cifra XOR

Aplica ciclicamente um XOR combinando os bytes da senha com os bytes do conteudo.

    >>> s = 'pizza'
    >>> t = 'Garoando'
    >>> xor_decifra('pizza', xor_cifra('pizza', t))
    'Garoando'

"""

import itertools
from getpass import getpass

CODIF = 'utf-8'

# `-> bytes` anotations em python 3
def xor_bytes(senha:bytes, conteudo:bytes) -> bytes:
    pares = zip(itertools.cycle(senha), conteudo)
    return bytes(a ^ b for a, b in pares)

def xor_cifra(senha:str, claro:str) -> bytes:
    saida = xor_bytes(senha.encode(CODIF), claro.encode(CODIF))
    return saida

def xor_decifra(senha:str, cifrado:bytes) -> str:
    saida = xor_bytes(senha.encode(CODIF), cifrado)
    return saida.decode(CODIF)

def main():
    import sys

    try:
        _, script, tipo, nome_entrada = sys.argv[1:]
    except ValueError:
        nome_entrada = input('Nome do arquivo: ')
        tipo = input('Qual o tipo da ação? (cifrar|decifrar): ')
    senha = getpass('Senha: ')

    if tipo == 'cifrar':
        print('Cifrando:', nome_entrada)

        with open(nome_entrada, 'rt') as arq_entrada:
            texto = arq_entrada.read()

        saida = xor_cifra(senha, texto)
        nome_arq_saida = nome_entrada + '.blob'

        with open(nome_arq_saida, 'wb') as arq:
            arq.write(saida)

    elif tipo == 'decifrar':
        print('Decifrando:', nome_entrada)

        with open(nome_entrada, 'rb') as arq:
            blob = arq.read()

        texto = xor_decifra(senha, blob)
        print(texto)

if __name__ == '__main__':
    main()