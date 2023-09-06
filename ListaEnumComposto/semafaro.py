'''
Projete uma função que receba como entrada a cor atual de um semáforo de trânsito e devolva a próxima cor que será ativada (considere um semáforo com três cores: verde, amarelo e vermelho).
'''

from enum import Enum,auto
from dataclasses import dataclass

@dataclass
class Cor(Enum):
     VERDE = auto()
     AMARELO = auto()
     VERMELHO = auto()

def verifica_proxima_cor(cor: Cor):
    '''
    Essa função recebe a cor atual de um semafaro como parametro, as cores são:
    verde, amarelo e vermelho. É retornado a proxima cor que vier da cor atual.
    Exemplos:
    >>> verifica_proxima_cor(Cor.VERDE).name
    'AMARELO'
    >>> verifica_proxima_cor(Cor.AMARELO).name
    'VERMELHO'
    >>> verifica_proxima_cor(Cor.VERMELHO).name
    'VERDE'
    '''
 
    if cor.name == Cor.VERDE.name:
        return Cor.AMARELO

    elif cor.name == Cor.AMARELO.name:
        return Cor.VERMELHO
    
    else:
        return Cor.VERDE
    
def main():
    op = int(input("Digite qual cor é a atual\n(1)VERDE\n(2)AMARELO\n(3)VERMELHO\nInsira a cor: "))
    if op == 1:
        c1 = Cor.VERDE  
    elif op == 2:
        c1 = Cor.AMARELO
    else:
        c1 = Cor.VERMELHO
    print(f"A Cor Atual do semafaro é {c1.name} e a proxima cor é {verifica_proxima_cor(c1).name}")

#main()
