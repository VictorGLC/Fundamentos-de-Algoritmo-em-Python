'''
Projete uma função que verifique se todos os elementos de uma lista de booleanos são falsos.
'''

def verifica_bool(lista: list) -> bool:
    for i in range(len(lista)):
        if lista[i] == True:
            return False

    return True

#print(verifica_bool([False,False]))
