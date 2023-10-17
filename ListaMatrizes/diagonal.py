'''
Matriz Diagonal:
Crie uma função que recebe uma matriz M[3][3] como entrada e calcula o maior elemento em sua diagonal principal.
Em seguida, divida todos os elementos da matriz M pelo maior valor encontrado 
e insira esses valores em uma nova matriz M2. A função deve retornar a matriz M2 como resultado.
'''

def diagonal(matriz: list) -> int:
  '''
  Retorna o maior elemento das diagonais de uma matriz quadrada
  Exemplos:
  >>> diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  9
  '''
  maior_valor_diagonal = matriz[0][0]

  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if i == j:
        if matriz[i][j] > maior_valor_diagonal:
          maior_valor_diagonal = matriz[i][j]

  return maior_valor_diagonal

def divisao_diagonal(matriz: list) -> list:
  '''
  >>> divisao_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  [[0.11, 0.22, 0.33], [0.44, 0.56, 0.67], [0.78, 0.89, 1.0]]
  '''
  m2: list = []
  maior_diagonal: int = diagonal(matriz)
  for i in range(len(matriz)):
    matriz_aux: list = []
    for j in range(len(matriz[i])):
      matriz_aux.append(round(matriz[i][j]/maior_diagonal, 2))
    m2.append(matriz_aux)

  return m2