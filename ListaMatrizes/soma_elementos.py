'''
Soma de Matriz 4x3:
Escreva uma função que recebe os elementos de uma matriz M[4][3] e retorna a soma de todos esses elementos.
'''
def cria_matriz(qt_linhas: int, qt_colunas: int, valor: int) -> list:
  '''
  Cria uma matriz baseado nos parametros linha, coluna e valor
  >>> cria_matriz(3, 3, 1)
  [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
  '''
  matriz = []
  
  for i in range(qt_linhas):
      linha = []
      for j in range(qt_colunas):
          linha.append(i + j + valor)
      matriz.append(linha)
  '''
  for i in range(qt_linhas):
      for j in range(qt_colunas):
          print("Elemento linha ", i, " e coluna ",j,": ", matriz[i][j])
  '''
  
  return matriz

def soma(matriz: list) -> int:
  '''
  >>> soma([[1, 2, 3], [4, 5, 6],[7, 8, 9], [10, 11, 12]])
  78
  >>> soma([[1, 1, 1], [1, 1, 1],[1, 1, 1], [1, 1, 1]])
  12
  '''
  soma: int = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        soma = soma + matriz[i][j]
  return soma