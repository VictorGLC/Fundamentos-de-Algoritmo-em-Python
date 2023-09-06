'''
Projete uma função que receba como entrada uma lista lst de números e crie uma nova lista colocando os valores negativos de lst antes dos positivos.
'''

def negative_before_positive(lst: list) -> list:
    '''
    Recebe uma lista de negativos e positivos e retorna uma outra lista colocando os numeros negativos antes dos positivos
    Exemplo:
    >>> negative_before_positive([2,3,4,-1,-2,-3,7,8,9])
    [-1, -2, -3, 2, 3, 4, 7, 8, 9]
    '''

    new_lst: list = []

    for i in range(len(lst)):
        if lst[i] < 0:
            new_lst.append(lst[i])

    for j in range(len(lst)):
        if lst[j] > 0:
            new_lst.append(lst[j])

    return new_lst
