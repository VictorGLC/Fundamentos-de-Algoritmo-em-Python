'''
Projete uma função que conte quantas vezes o valor mínimo de uma lista de inteiros não vazia aparece na lista.
'''

def minimal_value(lista: list) -> int:
    min: int = lista[0]
    for i in range(len(lista)):
        if lista[i] < min:
            min = lista[i]

    return min


def count_minimal_value(lista: list) -> int:
    minimo: int = minimal_value(lista)
    count: int = 0
    for i in range(len(lista)):
        if minimo == lista[i]:
            count=count+1

    return count

#print(count_minimal_value([2,1,1,1,6]))
