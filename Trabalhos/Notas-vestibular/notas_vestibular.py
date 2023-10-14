from dataclasses import dataclass

@dataclass
class Prova:
    codigo: str
    redacao: float
    respostas: list[int]

@dataclass
class Resultado:
    codigo: str
    nota_final: float

def somatorio_alternativas(s: int) -> list[int]:
    '''
    Calcula a lista de alternativas que somadas gera o somátorio *s*.
    Cada alternativa pode ser um dos valores: 1, 2, 4, 8, 16.
    Requer que *s* esteja no entre 0 e 31.
    Exemplos
    >>> somatorio_alternativas(8)
    [8]
    >>> somatorio_alternativas(16)
    [16]
    >>> somatorio_alternativas(15)
    [1, 2, 4, 8]
    >>> somatorio_alternativas(21)
    [1, 4, 16]
    >>> somatorio_alternativas(10)
    [2, 8]
    >>> somatorio_alternativas(31)
    [1, 2, 4, 8, 16]
    >>> somatorio_alternativas(22)
    [2, 4, 16]
    '''
    alternativas: list = []
    alternativa: int = 1
    while s > 0:
        # verifica se alternativa faz parte do somatório s
        if s % 2 == 1:
            alternativas.append(alternativa)
        # divide todas as alternativas que compõe
        # o somatório s por 2
        s = s // 2
        # procura a próxima alternativa
        alternativa = alternativa * 2
    return alternativas

def is_somatoria(respostas: list, gabarito: list) -> bool:
    '''
    Retorna se a questao é uma somatoria ou nao, ou seja, se tiver assinalado todas as respostas conforme o gabarito, 
    ou pelo menos uma resposta assinalado correta, porém, sem ter nenhuma alternativa incorreta assinalada
    Exemplos:
    >>> is_somatoria([4, 8], [2, 8])
    False
    >>> is_somatoria([4, 8, 16], [4, 8, 16])
    True
    >>> is_somatoria([4], [4, 8, 16])
    True
    '''
    for i in range(len(respostas)):
        if respostas[i] not in gabarito:
            return False
    return True 

def calcula_respostas(respostas: list[int], gabarito: list[int]) -> float:
    '''
    Recebe uma lista de respostas de somatoria com o gabarito e retorna o valor total dos acertos.
    >>> calcula_respostas([21, 8, 8, 8, 14], [21, 10, 8, 16, 15])
    19.5
    >>> calcula_respostas([4, 10, 4, 16, 10], [21, 10, 8, 16, 15])
    17.0
    >>> calcula_respostas([20, 0, 8, 16, 1], [21, 10, 8, 16, 15])
    17.5
    '''
    notas_acertos: list = []
    for i in range(len(gabarito)):
        # pega as alternativas da resposta e do gabarito
        resposta_alternativas_atuais: list = somatorio_alternativas(respostas[i])
        gabarito_alternativas_atuais: list = somatorio_alternativas(gabarito[i])

        valor_questao: int = 6/len(gabarito_alternativas_atuais)
        for j in range(len(resposta_alternativas_atuais)):
            if is_somatoria(resposta_alternativas_atuais, gabarito_alternativas_atuais):
                notas_acertos.append(valor_questao)

    return round(soma_recursiva(notas_acertos) * 100) / 100

def soma_recursiva(alternativas: list[int]) -> float:
    '''
    Recebe uma lista de inteiros e retorna a soma destes.
    >>> soma_recursiva([2.0, 3.0, 3.0, 6.0, 1.5, 1.5])
    17.0
    >>> soma_recursiva([2.0, 2.0, 2.0, 3.0, 6.0, 1.5, 1.5, 1.5])
    19.5
    '''
    if len(alternativas) == 0:
        return 0
    else:
        return alternativas[0] + soma_recursiva(alternativas[1:])

def resultado(provas: list[Prova], gabarito: list) -> list[Resultado]:
    '''
    Retorna o resultado final das provas.
    Exemplo:
    >>> resultado([Prova('3211', 80.0, [4, 10, 4, 16, 10]), Prova('7102', 0, [1, 2, 3, 4, 5]), Prova('1234', 90.0, [21, 8, 8, 8, 14]), Prova('5812', 32.0, [20, 0, 8, 16, 1]), Prova('9123', 0, [5, 4, 3, 2, 1])], [21, 10, 8, 16, 15])
    [Resultado(codigo='1234', nota_final=109.5), Resultado(codigo='3211', nota_final=97.0), Resultado(codigo='5812', nota_final=49.5)]
    '''
    resultado: list = []

    for i in range(len(provas)):
        if len(provas[i].respostas) == len(gabarito) and provas[i].redacao > 0:
            nota_final: float = provas[i].redacao + calcula_respostas(provas[i].respostas, gabarito)
            resultado.append(Resultado(provas[i].codigo, nota_final))

    return ordenar_lista(resultado)

def maior_resultado(resultados: list[Resultado]) -> Resultado:
    '''
    Retorna o maior resultado de uma lista de resultados
    Exemplo:
    >>> maior_resultado([Resultado(codigo='3211', nota_final=97.0), Resultado(codigo='1234', nota_final=109.5), Resultado(codigo='5812', nota_final=49.5)])
    Resultado(codigo='1234', nota_final=109.5)
    '''
    maior_resultado: Resultado = resultados[0]
    
    for i in range(len(resultados)):
        if resultados[i].nota_final > maior_resultado.nota_final:
            maior_resultado = resultados[i]

    return maior_resultado

def ordenar_lista(resultados: list[Resultado]) -> list[Resultado]:
    '''
    Retorna uma lista de resultado ordenada pelo maior valor das notas finais
    Exemplo:
    >>> ordenar_lista([Resultado(codigo='3211', nota_final=97.0), Resultado(codigo='1234', nota_final=109.5), Resultado(codigo='5812', nota_final=49.5)])  
    [Resultado(codigo='1234', nota_final=109.5), Resultado(codigo='3211', nota_final=97.0), Resultado(codigo='5812', nota_final=49.5)]
    '''
    resultado_ordenado: list[Resultado] = []
    
    for i in range(len(resultados)):
        maior: Resultado = maior_resultado(resultados)

        resultado_ordenado.append(maior)
        resultados = remover(resultados, maior)

    return resultado_ordenado

def remover(lista: list, elem) -> list:
    '''
    Retorna a lista sem o elemento dado como parametro.
    Exemplo:
    >>> remover(["laranja","maça","banana","laranja","beterraba"], "laranja")
    ['maça', 'banana', 'beterraba']
    '''
    nova_lista: list = []
    for i in range(len(lista)):
        if lista[i] != elem:
            nova_lista.append(lista[i])
    return nova_lista

def converte_string(respostas: list[str]) -> list[int]:
    '''
    Modifica uma lista de string por uma lista de inteiros que remove o 0 em unidades
    como 04, 08, 06, etc.
    '''
    for i in range(len(respostas)):
        if respostas[i][0] == 0:
            respostas[i] = int(respostas[i][1:])
        else:
            respostas[i] = int(respostas[i])

def main():
    """
    provas = [Prova(3211, 80.0, [4, 10, 4, 16, 10]), Prova(7102, 0, [1, 2, 3, 4, 5]), 
    Prova(1234, 90.0, [21, 8, 8, 8, 14]), Prova(5812, 32.0, [20, 0, 8, 16, 1]), Prova(9123, 0, [5, 4, 3, 2, 1])]
    gabarito = [21, 10, 8, 16, 15]
    """

    provas: list[Prova] = []
    gabarito: list[int] = []
    n_respostas: int = int(input("Digite o numero de questões: "))
    n_provas: int = int(input("Quantas provas deseja checar? "))

    for i in range(1, n_provas+1):
        print(f"{i}° Prova ")
        respostas: list[str] = []
        codigo = input("Digite o seu código: ")
        redacao = float(input("Digite o valor da redação: "))
        
        print(f"Digite as somatórias das suas respostas: ")
        for i in range(1, n_respostas+1):
            questao: str = input(f"Resposta - Questão {i}: ")
            respostas.append(questao)

        converte_string(respostas)
        prova = Prova(codigo,redacao, respostas)
        provas.append(prova)
        print("\n")

    print("Agora digite o gabarito das questões somatorias: \n")
    for i in range(1, n_respostas+1):
        questao: str = input(f"Gabarito - Questão {i}: ")
        gabarito.append(questao)
    
    converte_string(gabarito)
    resultados = resultado(provas, gabarito)
    print('O resultado do vestibular foi: \n')
    for i in range(len(resultados)):
        print(f"{i+1} lugar: Código: {resultados[i].codigo}, Nota: {resultados[i].nota_final}")

#main()