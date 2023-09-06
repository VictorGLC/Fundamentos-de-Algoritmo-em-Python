'''
Projete uma função que encontre o índice (posição) da primeira ocorrência do valor máximo em uma lista não vazia.
'''

def find_indice(lista: list) -> int:
    '''
    Recebe uma lista e encontra o indice da primeira ocorrencia do maior valor da lista
    >>> find_indice([150,50,300,100])
    2
    >>> find_indice([400,4,30,40])
    0
    >>> find_indice([50,400,20,400])
    1
    '''
    maximo: int = 0
    indice: int = 0

    for i in range(len(lista)):
        if maximo < lista[i]:
            maximo = lista[i]
            indice = i

    return indice

def main():
    #               0   1   2   3   4   5
    lista: list = [150,250,360,500,100,200]

    if len(lista) > 1:
        indice_maior_valor: int = find_indice(lista)
        print(f"O indice do primeiro maior valor é {indice_maior_valor}, do numero {lista[indice_maior_valor]}")
    else:
        print("Lista vazia")

#main()