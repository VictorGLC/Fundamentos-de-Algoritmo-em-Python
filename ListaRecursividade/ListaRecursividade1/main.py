def somar_numeros(n: int) -> int:
    '''
    Retorna a soma de todos os numeros menores ou iguais a n
    Exemplos:
    >>> somar_numeros(3)
    6
    >>> somar_numeros(2)
    3
    '''
    if n <= 1:
        return n 
    else:
        return (somar_numeros(n-1)) + n


def potencia(a: int, n: int) -> int:
    '''
    Retorna a potencia de uma base 'a' elevado a 'n'
    Exemplos:
    >>> potencia(0, 1)
    0
    >>> potencia(2, 3)
    8
    >>> potencia(3, 3)
    27
    >>> round(potencia(3, -2), 2)
    0.11
    '''
    if a == 0:
        return 0

    if n == 0:
        return 1
    elif n > 0:
        return a * potencia(a, n-1)
    else:
        return 1 / (a * potencia(a, -n-1)) 

def fatorial(n: int) -> int:
    '''
    Retorna o fatorial de um numero
    Exemplos:
    >>> fatorial(3)
    6
    >>> fatorial(4)
    24
    '''
    if n == 1:
        return n
    else:
        return fatorial(n-1) * n

def somas_sucessivas(n1: int, n2: int) -> int:
    '''
    Recebe dois numeros e retorna a soma sucessiva dos numeros,
    6x4 = 4+4+4+4+4+4 = 24
    Exemplos:
    >>> somas_sucessivas(6, 4)
    24
    >>> somas_sucessivas(4, 5)
    20
    >>> somas_sucessivas(6, -4)
    -24
    '''
    if n1 == 0:
        return 0
    elif n1 > 0:
        return n2 + somas_sucessivas(n1-1, n2)
    elif n1 < 0:
        return -somas_sucessivas(-n1, n2)

def serie(n: int) -> float:
    '''
    Retorna o calculo da serie ate n: 1 + 1/1! + 1/2! + ... + 1/n!
    Exemplos:
    >>> round(serie(3), 2)
    2.67
    >>> round(serie(2), 2)
    2.5
    >>> round(serie(4), 2)
    2.71
    '''
    if n == 0:
        return 1
    else:
        return 1/fatorial(n) + serie(n-1)
    
