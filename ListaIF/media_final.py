'''
Faça um programa em Python que receba a média final de um aluno e retorne seu conceito:

de 0,0 a 4,9: D;
de 5,0 a 6,9: C;
de 7,0 a 8,9: B;
de 9,0 a 10,0: A.
'''

def transforma_nota(media: float) -> str:
    '''
    Nesta função é dado a media final de um aluno, a qual 
    é retornado um valor de A até D conforme o valor de sua média
    A - 9.0 a 10.0
    B - 7.0 a 8.9
    C - 5.0 a 6.9
    D - 0.0 a 4.9
    Exemplos:
    >>> transforma_nota(10.0)
    'A'
    >>> transforma_nota(8.5)
    'B'
    >>> transforma_nota(6.5)
    'C'
    >>> transforma_nota(4.5)
    'D'
    >>> transforma_nota(11.0)
    'media invalida'
    '''

    if media >= 9.0 and media <= 10.0:
        return "A"
    elif media >= 7.0 and media <= 8.9:
        return "B"
    elif media >= 5.0 and media <= 6.9:
        return "C"
    elif media >= 0.0 and media <= 4.9:
        return "D"
    else: 
        return 'media invalida'


def main():
    media_final: float = float(input("Insira a media final do aluno: "))
    print(f"Seu conceito é: {transforma_nota(media_final)}")

main()
