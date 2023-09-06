'''
Dizemos que o nome de uma pessoa é curto se tem no máximo quatro letras e longo se tem mais de oito letras. Um nome que não é nem curto nem longo é considerado mediano. Projete uma função que classifique um nome de acordo com o número de letras
'''

from enum import Enum,auto
from dataclasses import dataclass

@dataclass
class Tamanho(Enum):
    CURTO = auto()
    MEDIO = auto()
    LONGO = auto()

def checa_tamanho(nome: str) -> Tamanho:
    '''
    Recebe um nome como parametro e retorna o tamanho do nome, ou seja, se o nome for menor ou igual a 4 caracteres sera um nome curto,
    se for menor que 8 e maior que 4 será um tamanho médio. Por fim, se o nome for maior a 8 caracteres será um nome longo.
    Exemplos
    >>> checa_tamanho("victor").name
    "MEDIO"
    >>> checa_tamanho("ana").name
    "CURTO"
    >>> checa_tamanho("lorrainny").name
    "LONGO"
    '''
    if len(nome) <= 4:
        return Tamanho.CURTO
    elif len(nome) > 8:
        return Tamanho.LONGO
    else:
        return Tamanho.MEDIO

def main():
    nome_pessoa = str(input("Digite o nome da pessoa: "))
    print(f"A pessoa com o nome {nome_pessoa} tem um nome de tamanho {checa_tamanho(nome_pessoa).name}.")

#main()

