'''
Sendo H = 1 + 1/2 + 1/3 + 1/4 + · · · + 1/N, faça uma função que receba por parâmetro o valor de N e calcule o valor de H.
'''

def calculate_h(n: int) -> float:
    '''
    Essa função recebe um numero n e retorna um valor somado de 1 + 1/2 + 1/3 + ... + 1/n
    Exemplo:
    >>> round(calculate_h(4),2)
    2.08
    '''
    h: float = 0
    
    for i in range(1, n+1):
        h = h + (1/i)

    return round(h,2)
