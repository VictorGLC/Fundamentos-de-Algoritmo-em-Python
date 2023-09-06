'''
Considere um jogo onde o personagem está em um tabuleiro (semelhante a um tabuleiro de jogo de xadrez). As linhas e colunas do tabuleiro são numeradas de 1 a 10, dessa forma, é possível representar a posição (casa) do personagem pelo número da linha e da coluna em que ele se encontra. O personagem fica virado para uma das direções: norte, sul, leste ou oeste. O jogador pode avançar o seu personagem qualquer número de casas na direção em que ele está virado, mas é claro, não pode sair do tabuleiro. Projete uma função que indique, a partir das informações do personagem, qual é o número máximo de casas que ele pode avançar na direção em que está virado.
'''

from dataclasses import dataclass

@dataclass
class Tabuleiro:
    linha: int
    coluna: int
    direcao: str

def direcao_andar(t1: Tabuleiro) -> int:
    '''
    Essa funcao recebe um tipo composto Tabuleiro que retorna o numero de casas que uma peça pode andar na direcao dada.
    Ou seja, a funcao recebe as coordenadas de onde a peça esta no tabuleiro (tabuleiro 10x10) e a direcao que a peça esta virada.
    Exemplos:
    >>> direcao_andar(Tabuleiro(1,1,"norte"))
    9
    >>> direcao_andar(Tabuleiro(5,5,"oeste"))
    4
    >>> direcao_andar(Tabuleiro(5,5,"leste"))
    5
    >>> direcao_andar(Tabuleiro(10,10,"sul"))
    9
    '''
    if t1.direcao == "norte":
        casas = norte(t1.coluna)
    elif t1.direcao == "sul":
        casas = sul(t1.coluna)
    elif t1.direcao == "leste":
        casas = leste(t1.linha)
    elif t1.direcao == "oeste":
        casas = oeste(t1.linha)
    else:
        casas = 0

    return casas

def norte(coluna: int) -> int:
    '''
    Retorna o numero de casas que uma peça pode andar para o norte
    Exemplos:
    >>> norte(1)
    9
    >>> norte(10)
    0
    '''
    if coluna>0 and coluna <=10:
        casas = 10 - coluna

    return casas

def sul(coluna: int) -> int:
    '''
    Retorna o numero de casas que uma peça pode andar para o sul
    Exemplos:
    >>> sul(10)
    9
    >>> sul(1)
    0
    '''
    if coluna>0 and coluna<=10:
        casas = coluna - 1

    return casas

def oeste(linha: int) -> int:
    '''
    Retorna o numero de casas que uma peça pode andar para o oeste
    Exemplos:
    >>> oeste(10)
    9
    >>> oeste(1)
    0
    '''
    if linha>0 and linha <=10:
        casas = linha - 1

    return casas

def leste(linha: int) -> int:        
    '''
    Retorna o numero de casas que uma peça pode andar para o leste
    Exemplos:
    >>> leste(1)
    9
    >>> leste(10)
    0
    '''

    if linha>0 and linha <=10:
        casas = 10 - linha

    return casas


def main():
    linha = int(input("Digite a posição da linha em que o jogador está: "))
    coluna = int(input("Digite a posição da coluna em que o jogador está: "))
    direcao = str(input("Em qual direção ele está: "))

    tab = Tabuleiro(linha,coluna,direcao)
    casas_andadas = direcao_andar(tab)

    if (linha > 10 or linha < 1) or (coluna > 10 or coluna < 1):
        print("Jogador fora do tabuleiro")
    else:  
        print(f"O jogador pode andar para {tab.direcao}, {casas_andadas} casas")


#main()
