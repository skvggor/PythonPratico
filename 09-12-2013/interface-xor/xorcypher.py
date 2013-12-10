"""
XOR: cifra que aplica ciclicamente um XOR, combinando os bytes da senha com os bytes do conteúdo.

  >>> s = 'pizza'
  >>> t = 'garoando'
  >>> xor_decypher('pizza', xor_cypher('pizza', t))
  'garoando'
"""

import itertools
COD = 'utf-8'

def xor_bytes(senha, conteudo):
  pares = zip(itertools.cycle(senha), conteudo)
  return bytes(a ^ b for a, b in pares)

def xor_cypher(senha, limpo):
  saida = xor_bytes(senha.encode(COD), limpo.encode(COD))
  return saida

def xor_decypher(senha, cifrado):
  saida = xor_bytes(senha.encode(COD), cifrado)
  return saida.decode(COD)