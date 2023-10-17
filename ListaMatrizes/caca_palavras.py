'''
Escreva uma função que construa um caça-palavras em uma matriz.
Suponha que M seja uma matriz de caracteres e s seja uma palavra. A função deve indicar 
todas as ocorrências de s na matriz. Suponha que as palavras s são lidas da esquerda 
para a direita (na linha) ou de cima para baixo (na coluna). Você pode supor que todas 
as letras são maiúsculas. Por exemplo, suponha que M seja:

```
M = [['A', 'C', 'A', 'S', 'A', 'M', 'C', 'A', 'S', 'W', 'B'],
    ['C', 'A', 'X', 'R', 'F', 'T', 'P', 'A', 'S', 'A', 'C'],
    ['A', 'S', 'X', 'I', 'E', 'J', 'H', 'W', 'T', 'Q', 'A'],
    ['S', 'A', 'E', 'O', 'W', 'M', 'Q', 'Z', 'O', 'D', 'B'],
    ['A', 'C', 'Y', 'K', 'F', 'W', 'C', 'A', 'A', 'V', 'B']]
```

Se a palavra s for "CASA", então ela ocorre na linha 0 da coluna 1 até a coluna 4;
na coluna 0 da linha 1 até a linha 4; e na coluna 1 da linha 0 até a linha 3. 
A função deve identificar todas as ocorrências da palavra s na matriz.
'''

def cria_caca_palavras(qtde_linhas, qtde_colunas) -> list:
  '''
  Retorna um caça palavras inserido pelo usuario como por exemplo um com 5 linhas e 11 colunas:
  [['A', 'C', 'A', 'S', 'A', 'M', 'C', 'A', 'S', 'W', 'B'], ['C', 'A', 'X', 'R', 'F', 'T', 'P', 'A', 'S', 'A', 'C'],
   ['A', 'S', 'X', 'I', 'E', 'J', 'H', 'W', 'T', 'Q', 'A'], ['S', 'A', 'E', 'O', 'W', 'M', 'Q', 'Z', 'O', 'D', 'B'], 
   ['A', 'C', 'Y', 'K', 'F', 'W', 'C', 'A', 'A', 'V', 'B']]
  '''
  matriz: list = []

  for i in range(qtde_linhas):
    linha: list = []
    for j in range(qtde_colunas):
      letra: str = input(f"Digite a letra da posicao [{i}][{j}]: ")
      linha.append(letra)
    matriz.append(linha)

  return matriz

def achar_palavra(s: str, M: list) -> list:
  '''
  >>> achar_palavra('CASA', [['A', 'C', 'A', 'S', 'A', 'M', 'C', 'A', 'S', 'W', 'B'], ['C', 'A', 'X', 'R', 'F', 'T', 'P', 'A', 'S', 'A', 'C'], ['A', 'S', 'X', 'I', 'E', 'J', 'H', 'W', 'T', 'Q', 'A'], ['S', 'A', 'E', 'O', 'W', 'M', 'Q', 'Z', 'O', 'D', 'B'], ['A', 'C', 'Y', 'K', 'F', 'W', 'C', 'A', 'A', 'V', 'B']])
  [[(0, 1), (0, 2), (0, 3), (0, 4)], [(0, 1), (1, 1), (2, 1), (3, 1)], [(1, 0), (2, 0), (3, 0), (4, 0)]]
  '''
  ocorrencias = []
  linha = len(M)
  coluna = len(M[0])
  len_s = len(s)

  for i in range(linha):
      for j in range(coluna):
          # Verifica a ocorrência da palavra na horizontal (esquerda para a direita)
          if j + len_s <= coluna and M[i][j:j + len_s] == list(s):
              ocorrencias.append([(i, c) for c in range(j, j + len_s)])

          # Verifica a ocorrência da palavra na vertical (de cima para baixo)
          if i + len_s <= linha and [M[i + r][j] for r in range(len_s)] == list(s):
              ocorrencias.append([(i + r, j) for r in range(len_s)])

  return ocorrencias