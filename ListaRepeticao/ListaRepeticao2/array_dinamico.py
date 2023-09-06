'''
Projete uma função que receba como entrada um array dinâmico de números, uma posição i e um número n, e devolva um novo array com n adicionado na posição i do array de entrada.
'''

def add_element(lista: list, index: int, num: int) -> list:
    new_list: list = []

    for i in range(index):
        new_list.append(lista[i])

    new_list.append(num)
    
    for i in range(index, len(lista)):
        new_list.append(lista[i])

    return new_list

#print(add_element([1,2,3,4],2,4))
