'''
Faça uma função que receba uma lista de caracteres e mais dois caracteres, C1 e C2. Crie uma nova lista trocando todas as ocorrências de C1 por C2.
'''

def change_characters(lista: list, c1: str, c2: str) -> list:
    '''
    Recebe uma lista de caracteres e retorna trocado todas as ocorrencias de c1 por c2
    Exemplo:
    >>> change_characters(['a','b','c','d','e','b'], 'b', 'd')
    ['a', 'd', 'c', 'd', 'e', 'd']
    '''
    new_list: list = []

    for i in range(len(lista)):
        if lista[i] == c1:
            new_list.append(c2)
        else:
            new_list.append(lista[i])

    return new_list

