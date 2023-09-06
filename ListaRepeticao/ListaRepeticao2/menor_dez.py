'''
Projete uma função que verifique se todos os elementos de uma lista de inteiros são menores que 10.
'''

def menor_dez(lista: list) -> bool:
    resp = True
    for i in range(len(lista)):
        if lista[i] > 10:
            resp = False
    
    return resp

#print(menor_dez([2,3,4,51,6,7,8,9]))
