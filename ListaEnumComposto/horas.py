'''
Escreva uma função que receba um número inteiro que representa um intervalo de tempo medido em minutos e devolva uma estrutura contendo o número equivalente de horas e minutos (por exemplo, 131 minutos equivalem a 2 horas e 11 minutos). Use um tipo composto que tenha um campo para horas (inteiro) e um campo para minutos (inteiro).
'''

from dataclasses import dataclass

@dataclass
class Horario:
    horas: int
    minutos: int

def converte_minutos(minutos: int) -> Horario:
    '''
    Recebe o valor no parametro em minutos e retorna o valor convertido em horas.
    Exemplos:
    >>> (converte_minutos(131).horas, converte_minutos(131).minutos)
    (2, 11)
    >>> (converte_minutos(90).horas, converte_minutos(90).minutos)
    (1, 30)
    >>> (converte_minutos(180).horas, converte_minutos(180).minutos)
    (3, 0)
    '''
    horas = minutos//60
    minutos = round(((minutos/60)-horas)*60)
    horario_convertido = Horario(horas,minutos)
    return horario_convertido

def main():
    minutos_entrada = int(input("Digite os minutos: "))
    valor_horas = converte_minutos(minutos_entrada).horas
    valor_minutos = converte_minutos(minutos_entrada).minutos
    print(f"Os minutos convertidos para hora são: {valor_horas} horas e {valor_minutos} minutos")

#main()    
