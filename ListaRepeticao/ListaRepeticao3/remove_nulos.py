'''
Projete uma função que crie uma nova lista removendo todos os valores nulos de uma lista de inteiros.
'''

def remove_nulls(lista: list) -> list:
    '''
    Recebe uma lista com valores nulos e inteiros, retorna a mesma lista porem sem os valores nulos.  
    Exemplos:
    >>> remove_nulls([2,3,4,0,4,3])
    [2, 3, 4, 4, 3]
    '''

    new_list = []

    for i in range(len(lista)):
        if lista[i] != 0:
            new_list.append(lista[i])

    return new_list

