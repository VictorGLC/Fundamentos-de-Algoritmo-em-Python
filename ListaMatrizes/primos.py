'''
Números Primos até N:
Escreva uma função que receba um número inteiro N e retorne uma lista com todos os números primos até N.
'''

def verifica_primo(n: int) -> bool:
  '''
  Retorna se um numero é primo ou não
  >>> verifica_primo(11)
  True
  >>> verifica_primo(8)
  False
  >>> verifica_primo(2)
  True
  '''
  for i in range(2, n):
    if n % i == 0 and n != i:
      return False 
  return True

def primo(n: int) -> list:
  '''
  Retorna uma lista de numeros primos ate um determinado numero n.
  >>> primo(11)
  [1, 2, 3, 5, 7, 11]
  '''
  lst: list = []
  for i in range(1, n+1):
    if verifica_primo(i):
      lst.append(i)

  return lst