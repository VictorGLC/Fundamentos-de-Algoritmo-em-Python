'''
Segundo a Wikipédia, um pixel é o menor elemento de um dispositivo de exibição, como, por exemplo, um monitor, ao qual é possível atribuir uma cor. Nos monitores atuais, os pixels são organizados em linhas e colunas, formando a imagem exibida. Cada pixel pode ser referenciado por uma coordenada, que é o número da linha e coluna em que ele aparece. Por exemplo, em um monitor de 1920 colunas por 1080 linhas, o pixel no canto superior esquerdo está na posição (0, 0), enquanto o pixel no canto inferior direito está na posição (1919, 1079).

Em um ambiente gráfico com janelas, quando o usuário faz um clique com o mouse, é necessário identificar em qual janela ocorreu o clique.

(b) (Desafio) Projete uma função que verifique se as áreas de duas janelas se sobrepõem.
'''

from dataclasses import dataclass

@dataclass
class Janela:
    x1: int
    y1: int
    x2: int
    y2: int
    
def tela_sobreposta(janela: Janela, outra_janela: Janela) -> bool:
    '''
    Recebe duas janelas e verifica se as duas janelas estao sobrepostas uma a outra
    Exemplos:
    >>> tela_sobreposta(Janela(100, 100, 300, 200), Janela(200, 150, 400, 250))
    True
    >>> tela_sobreposta(Janela(100, 100, 300, 200), Janela(400, 300, 500, 400))
    False
    '''
    # Verificar se a janela atual está à esquerda ou à direita da outra janela
    if janela.x2 < outra_janela.x1 or janela.x1 > outra_janela.x2:
        return False
        
    # Verificar se a janela atual está acima ou abaixo da outra janela
    if janela.y2 < outra_janela.y1 or janela.y1 > outra_janela.y2:
        return False
        
    # Se nenhuma das condições acima for atendida, há sobreposição
    return True

def main():
    janela1 = Janela(100, 100, 300, 200)
    janela2 = Janela(200, 150, 400, 250)

    # Verificar sobreposição
    if tela_sobreposta(janela1, janela2):
        print("As janelas se sobrepõem.")
    else:
        print("As janelas não se sobrepõem.")

     
#main()

