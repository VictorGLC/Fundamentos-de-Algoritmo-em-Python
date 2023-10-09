# Nota no Vestibular

Este é um projeto para resolver o problema de calcular a nota de cada candidato em um vestibular da Universidade Estadual de Maringá (UEM) após uma queda de energia que corrompeu o disco que armazenava o programa original. O objetivo é recuperar o programa e salvar o vestibular da UEM.

## Problema

O primeiro desafio é entender como o gabarito e as respostas são representados e como calcular a nota de cada questão. As informações sobre o cálculo da nota estão no manual do candidato (página 21).

Baseado nessas informações, a nota para uma lista com 5 questões, cujas respostas assinaladas foram [16, 5, 0, 5, 2] e cujo o gabarito é [23, 7, 0, 12, 18], é 14.5 (1.5 + 4.0 + 6.0 + 0.0 + 3.0).

## Função para Calcular a Lista de Alternativas

Calculamos a nota de uma questão mais facilmente se tivermos uma lista das alternativas corretas e uma lista das alternativas assinaladas. A função a seguir converte um valor de somatório em uma lista com as alternativas correspondentes.

```python
def somatorio_alternativas(s: int) -> list[int]:
    '''
    Calcula a lista de alternativas que somadas geram o somatório *s*.
    Cada alternativa pode ser um dos valores: 1, 2, 4, 8, 16.
    Requer que *s* esteja entre 0 e 31.
    
    Exemplos
    >>> somatorio_alternativas(0)
    []
    >>> somatorio_alternativas(1)
    [1]
    >>> somatorio_alternativas(21)
    [1, 4, 16]
    >>> somatorio_alternativas(10)
    [2, 8]
    >>> somatorio_alternativas(31)
    [1, 2, 4, 8, 16]
    '''
    alternativas = []
    alternativa = 1
    while s > 0:
        # verifica se a alternativa faz parte do somatório s
        if s % 2 == 1:
            alternativas.append(alternativa)
        # divide todas as alternativas que compõem o somatório s por 2
        s = s // 2
        # procura a próxima alternativa
        alternativa = alternativa * 2
    return alternativas
```
Cada prova tem um código de candidato (número), uma nota da redação (de 0 a 120) e uma lista com a resposta
das questões da prova. 

Você deve projetar uma função que receba como entrada uma lista de provas e um gabarito
e devolva uma lista com o desempenho de cada candidato que não foi desclassificado na redação (não ficou com nota
zero).

| Código  | Redação | Respostas |
|-------------|-------------|-------------|
| 3211 | 80 | 04 10 04 16 10 |
| 7102 | 0 | 01 02 03 04 05 |
| 1234 | 90 | 21 08 08 08 14 |
| 5812 | 32 | 20 00 08 16 01 |
| 9123 | 0 | 05 04 03 02 01 |

Considerando que o gabarito é 21 10 08 16 15, a função deve gerar como resposta

| Código  | Nota |
|-------------|-------------|
| 1234 | 109,5 | 
| 3211 | 97,0 | 
| 5812 | 49,5 |

Note que a quantidade de itens na lista de resposta de cada candidato é igual a quantidade de itens no gabarito e essa
quantidade pode variar.

Note também que os candidatos na resposta estão classificados por nota.

Seu projeto de resolução do problema deve incluir pelo menos uma função recursiva e uma função que modifique uma
lista passada por parâmetro.
