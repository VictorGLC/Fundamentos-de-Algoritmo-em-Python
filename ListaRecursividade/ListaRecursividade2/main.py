# 1. Projete uma funcao recursiva que some os elementos de um arranjo.

def soma_lista(lista: list) -> int:
    '''
    Retorna a soma de todos os elementos do arranjo
    Exemplos:
    >>> soma_lista([1,2,3,4,5,6])
    21
    >>> soma_lista([10,20,30,50])
    110
    '''

    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

# 2. Projete uma funcao recursiva que conte quantas vezes um determinado valor
# aparece em um arranjo.
def conta_numero(lista: list, n: int) -> int:
    '''
    Retorna quantas vezes um valor n apareceu no arranjo
    Exemplos:
    >>> conta_numero([1,1,2,3,5], 1)
    2
    >>> conta_numero([12,34,534,543,12,34], 12)
    2
    >>> conta_numero([1,6,4,6,6,6,9,10], 6)
    4
    '''

    if len(lista) == 0:
        return 0
    else:   
        if lista[0] == n:
            return conta_numero(lista[1:], n) + 1
        else:
            return conta_numero(lista[1:], n)

# 3. Projete uma funcao recursiva que verifique se os elementos de um arranjo estao
# em ordem nao decrescente. 
def verifica_decrescente(lista: list) -> bool:
    '''
    Verifica se uma lista é decrescente
    Exemplos:
    >>> verifica_decrescente([8,6,5,3,2,1])
    True
    >>> verifica_decrescente([20,30,10,5,1])
    False
    >>> verifica_decrescente([100,500,300])
    False
    '''
    if len(lista) <= 1:
        return True
    else:
        if lista[0] >= lista[1]:
            return verifica_decrescente(lista[1:])
        else:
            return False

# 4. Um arranjo de numeros é chamado de arranjo binario se todos os seus elementos
# sao 0 ou 1. Projete uma funcao recursiva que verifique se um arranjo é binario

def verifica_binario(lista: list) -> bool:
    '''
    Verifica se uma lista é binaria
    Exemplos:
    >>> verifica_binario([1,0,1,0,0,0,1,1,1])
    True
    >>> verifica_binario([2,1,1,1,0,0,1,0])
    False
    '''
    if len(lista) <= 1:
        return True
    else:
        if lista[0] == 1 or lista[0] == 0:
            return verifica_binario(lista[1:])
        else:
            return False

# 5. Projete uma funcao recursiva que encontre o valor maximo de um arranjo nao
# vazio. Dica: considere o caso base para arranjo de tamanho == 1.

def valor_maximo(lista: list) -> int:
    '''
    Retorna o maior valor de uma lista de inteiros
    Exemplos:
    >>> valor_maximo([2,3,4,5,6,7])
    7
    >>> valor_maximo([323, 231, 122, 35, 122])
    323
    >>> valor_maximo([1,2,3,400,5,6,7])
    400
    >>> valor_maximo([1,2,300,500,60,70])
    500
    '''
    if len(lista) == 1:
        return lista[0]
    else:
        if lista[0] > valor_maximo(lista[1:]):
            return lista[0]
        else:
            return valor_maximo(lista[1:])

# 6. Projete uma funcao recursiva que verifique se todos os elementos de um arranjo
# sao pares.

def verifica_pares(lista: list) -> bool:
    '''
    Retorna se todos os elementos da lista sao pares
    Exemplos:
    >>> verifica_pares([2,4,6,10,20,800])
    True
    >>> verifica_pares([20,30,50,25,40])
    False
    '''
    if len(lista) <= 1:
        return True
    else:
        if lista[0] % 2 == 0:
            return verifica_pares(lista[1:])
        else:
            return False