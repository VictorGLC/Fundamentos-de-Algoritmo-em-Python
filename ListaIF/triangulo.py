'''
Escreva uma função em Python que receba 3 valores reais X, Y e Z e que verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso, retorne qual o tipo de triângulo formado. Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma do comprimento dos outros dois lados. Caso seja possível formar o triângulo, o programa deve identificar o tipo de triângulo formado observando as seguintes definições: Triângulo Equilátero: os comprimentos dos 3 lados são iguais. Triângulo Isósceles: os comprimentos de 2 lados são iguais. Triângulo Escaleno: os comprimentos dos 3 lados são diferentes. OBS: seu programa deve ter duas funções: uma que valida o triângulo e outra que identifica o tipo dele.
'''

def is_triangulo(x: int, y: int, z: int) -> bool:
    '''
    A função tem como parametro os tres lados de um triangulo. O objetivo desta função é verificar
    se os lados formam um triangulo. Para que isso seja verdade cada lado do triangulo tem que ser
    menor do que a soma dos outros lados. Ou seja: x<y+z, y<x+z, z<x+y
    Exemplos:   
    >>> is_triangulo(20,15,5)
    False
    >>> is_triangulo(12,12,12)
    True
    >>> is_triangulo(12,24,35)
    True
    >>> is_triangulo(12,24,24)
    True
    '''

    return (x < y+z and y < x+z and z < x+y)

def tipo_triangulo(x: int,y: int,z: int) -> str:
    '''
    Esta função recebe como parametro os tres lados de um triangulo e calcula se o triangulo é equilatero, isosceles ou escaleno.
    Um triangulo equilatero tem 3 lados iguais, o isosceles tem 2 lados iguais e o escaleno tem todos os lados diferentes.
    Exemplos:
    >>> tipo_triangulo(12,12,12)
    'equilatero'
    >>> tipo_triangulo(12,24,35)
    'escaleno'
    >>> tipo_triangulo(24,24,12)
    'isosceles'
    >>> tipo_triangulo(24,12,24)
    'isosceles'
    >>> tipo_triangulo(12,24,24)
    'isosceles'
    '''

    equilatero: bool = (x==y and x==z)
    isosceles: bool = (x == y and x != z) or (y == z and y != x) or (z == x and z != y)

    if equilatero:
        return 'equilatero'
    elif isosceles:
        return 'isosceles'
    else:
        return 'escaleno'
 

def main():
    x: int = int(input("Insira o valor do lado x: "))
    y: int = int(input("Insira o valor do lado y: "))
    z: int = int(input("Insira o valor do lado z: "))

    if is_triangulo(x,y,z):
        print(f"É um triângulo {tipo_triangulo(x,y,z)}")
    else: 
        print("Não é um triângulo")

main() 
