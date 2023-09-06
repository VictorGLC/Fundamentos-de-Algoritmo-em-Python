'''
Proposta do problema:
Faça funções em Python que leiam as idades de 4 pessoas, calculem e depois informem a média das idades e a idade da pessoa mais velha.
'''

def maximo(n1: int, n2: int) -> int:
    '''
    Nesta função é recebido dois parametros sendo eles dois valores, aos quais são comparados e retornado o maior valor dentre eles.
    Exemplos:
    >>> maximo(12,24)
    24
    >>> maximo(54,98)
    98
    '''
    if n1>n2:
        return n1
    else:
        return n2

def mais_velho(id1: int,id2: int,id3: int,id4: int) -> int:
    '''
    Esta função recebe como parametros a idade de 4 pessoas e verifica qual das idades é a maior dentre elas
    Exemplos:
    >>> mais_velho(12,24,54,98)
    98
    >>> mais_velho(34,89,12,56)
    89
    >>> mais_velho(46,10,16,18)
    46
    '''

    return maximo(maximo(id1,id2), maximo(id3,id4))


def media_idades(id1: int,id2: int,id3: int,id4: int) -> float:
    '''
    Esta função recebe 4 idades de pessoas e retorna a média aritmetica dentre elas.
    Exemplos:
    >>> media_idades(12,24,54,98)
    47.0
    >>> media_idades(34,89,12,56)
    47.75
    >>> media_idades(46,10,16,18)
    22.5
    '''

    soma = id1+id2+id3+id4

    return soma/4

def main():
    id1=int(input("Digite a idade da primeira pessoa: "))
    id2=int(input("Digite a idade da segunda pessoa: "))
    id3=int(input("Digite a idade da terceira pessoa: "))
    id4=int(input("Digite a idade da quarta pessoa: "))

    print(f"A média aritmetíca das idades é: {media_idades(id1,id2,id3,id4)}\nA idade mais velha é: {mais_velho(id1,id2,id3,id4)}")

main()

