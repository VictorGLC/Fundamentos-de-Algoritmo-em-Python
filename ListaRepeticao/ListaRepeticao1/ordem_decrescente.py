'''
Projete uma função que verifique se uma lista de valores está em ordem não decrescente.
'''

def esta_em_ordem_decrescente(lista: list) -> bool:
    '''ordem_decrescente.py
    Recebe uma lista e verifica se esta em ordem decrescente
    Exemplos:
    >>> esta_em_ordem_decrescente([40,30,20,10,5,1])
    True
    >>> esta_em_ordem_decrescente([50,56,40,30,5,1])
    False
    >>> esta_em_ordem_decrescente([50,45,40,30,5,60])
    False
    '''
    valor_anterior: int = lista[0]
    for i in range(1, len(lista)):
        if valor_anterior <= lista[i]:
            return False

        valor_anterior = lista[i]

    return True


def main():
    lista = [300,200,20,10,5,1]

    if esta_em_ordem_decrescente(lista):
        print("A lista esta em ordem decrescente")
    else: 
        print("A lista não esta em ordem decrescente")

#main()