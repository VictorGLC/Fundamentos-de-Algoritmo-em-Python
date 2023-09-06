'''
Projete uma função que crie uma nova lista somando um valor x especificado a cada elemento de uma lista de inteiros.
'''

def cria_lista(lista: list, num: int) -> list:
    new_lista: list = []
    for i in range(len(lista)):
        new_lista.append(lista[i]+num)

    return new_lista

#print(cria_lista([2,3,4,5], 2))
