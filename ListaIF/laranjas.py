'''
Um supermercado está fazendo uma promoção de laranjas. Elas custam R$0,35 cada se forem compradas menos do que uma dúzia, e R$0,30 se forem compradas pelo menos doze. Escreva uma função em Python que receba o número de laranjas compradas, calcule e retorne o valor total da compra para ser informado.
'''

def custo_laranja(quantidade: int) -> float:
    '''
    Esta função recebe uma quantidade como parametro da função e retorna o custo de laranjas
    conforme o seguinte:
    caso a quantidade seja igual ou superior a 12 unidades, cada produto custará R$0.30
    caso a quantidade seja menor que 12 unidades, cada produto custará R$0.35
    Exemplos:
    >>> round(custo_laranja(12),2)
    3.6
    >>> round(custo_laranja(6),2)
    2.1
    >>> round(custo_laranja(24),2)
    7.2
    >>> round(custo_laranja(11),2)
    3.85
    '''
    if quantidade >= 12:
        return quantidade * 0.3
    else:
        return quantidade * 0.35

def main():
    quant: int = int(input("Digite a quantidade de laranjas que deseja comprar: "))
    valor_laranjas: float = round(custo_laranja(quant), 2)
    print(f"O custo da laranja é R${valor_laranjas}")

main()
