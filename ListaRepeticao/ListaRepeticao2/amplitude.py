'''
Projete uma função que calcule a amplitude dos valores de uma lista não vazia de números, isto é, a diferença entre o maior e o menor valor da lista.
'''

def minimal_value(lista: list) -> int:
    min: int = lista[0]
    for i in range(len(lista)):
        if lista[i] < min:
            min = lista[i]

    return min

def max_value(lista: list) -> int:
    max: int = lista[0]
    for i in range(len(lista)):
        if max < lista[i]:
            max = lista[i]

    return max

def amplitude(lista: list) -> int:
    maximo = max_value(lista)
    minimo = minimal_value(lista)

    return maximo - minimo

print(amplitude([3,5,6,8]))
