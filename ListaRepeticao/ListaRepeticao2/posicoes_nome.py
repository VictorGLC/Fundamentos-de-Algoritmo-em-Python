'''
Projete uma função que encontre as posições de todas as ocorrências de um nome em uma lista de nomes.
'''

def find_name(lista: list, name: str) -> list:
    posicoes:list = []
    for i in range(len(lista)):
        if lista[i] == name:
            posicoes.append(i)

    return posicoes

#print(find_name(["vsictor","victsaor","vicsator","jose"], "victor"))

