'''
Uma eleição é realizada com apenas dois candidatos. Cada eleitor pode votar no primeiro candidato, no segundo candidato ou votar em branco. O candidato que tiver mais votos ganha a eleição. Se os votos em branco forem mais do que 50% do total de votos, novas eleições devem ser convocadas. Projete uma função que receba como entrada uma lista não vazia de votos e determine o resultado da eleição. Dica: suponha a existência de uma função auxiliar que conte votos de um tipo especificado por parâmetro. Em um segundo momento, desenvolva essa função.
'''

def maximo_votos(lista_votos: list) -> int:
    '''
    Recebe uma lista e retorna o valor total dos numeros da lista
    Exemplos:
    >>> maximo_votos([2,4,5,6,7,8,10])
    42
    '''
    soma: int = 0
    for i in range(len(lista_votos)):
        soma+=lista_votos[i]

    return soma

def resultado_eleicao(votos_candidato1: list, votos_candidato2: list, votos_nulos: list) -> str:
    '''
    Recebe tres listas com votos dos candidatos e retorna o candidato vencedor
    >>> resultado_eleicao([2,4,6,8], [2,2,3,1], [5,2])
    'Candidato 1'
    >>> resultado_eleicao([2,4,1], [2,2,3,1], [4,1])
    'Candidato 2'
    >>> resultado_eleicao([2,4,1], [2,3,4], [5,6,8,10])
    'Nulo'
    '''

    total_candidato1: int = maximo_votos(votos_candidato1)
    total_candidato2: int = maximo_votos(votos_candidato2)
    total_nulos: int = maximo_votos(votos_nulos)

    total_votos: int = total_candidato1 + total_candidato2 + total_nulos
    
    vencedor: str = ""

    if total_nulos > (total_votos/2):
        vencedor = "Nulo"
    elif  total_candidato1 > total_candidato2:
        vencedor = "Candidato 1"
    else:
        vencedor = "Candidato 2"
 
    return vencedor

def cria_lista():
    '''
    Cria uma lista com um tamanho determinado
    '''
    lista=[]
    n = int(input("Qual o tamanho da Lista?: "))
    for i in range(n):
        lista.append(int(input(f"Digite o {i+1} valor: ")))

    return lista

def main():
    print("Digite a lista com os votos de cada candidato e os votos nulos: ")
    print("\nCandidato 1:")
    candidato1: list = cria_lista()
    print("\nCandidato 2:")
    candidato2: list = cria_lista()
    print("\nNulos:")
    nulos: list = cria_lista()
    
    vencedor: str = resultado_eleicao(candidato1,candidato2,nulos)
    
    if vencedor == 'Nulo':
        print("\nA maioria dos votos foram nulos, faremos outra eleição.\n")
        print('Recomeçando as eleições...\n')
        main()
    else:
        print(f"\nO vencedor é:\n{resultado_eleicao(candidato1, candidato2, nulos)}")

main()
