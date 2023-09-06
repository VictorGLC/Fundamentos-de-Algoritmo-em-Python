'''
Segundo a Wikipédia, um pixel é o menor elemento de um dispositivo de exibição, como, por exemplo, um monitor, ao qual é possível atribuir uma cor. Nos monitores atuais, os pixels são organizados em linhas e colunas, formando a imagem exibida. Cada pixel pode ser referenciado por uma coordenada, que é o número da linha e coluna em que ele aparece. Por exemplo, em um monitor de 1920 colunas por 1080 linhas, o pixel no canto superior esquerdo está na posição (0, 0), enquanto o pixel no canto inferior direito está na posição (1919, 1079).

Em um ambiente gráfico com janelas, quando o usuário faz um clique com o mouse, é necessário identificar em qual janela ocorreu o clique.

(a) Projete uma função que receba como parâmetros as informações sobre uma janela e um clique do mouse, e determine se o clique aconteceu sobre a janela.
'''

from dataclasses import dataclass

@dataclass
class Janela:
    altura: int
    largura: int

def clicou_na_tela(janela: Janela, coord_x: int, coord_y: int) -> bool:
    '''
    Recebe as informaçoes de uma janela e verifica se as coordenadas do mouse estao nesta janela
    Exemplos:
    >>> clicou_na_tela(Janela(1920,1080), 1,1)
    True
    >>> clicou_na_tela(Janela(1920,1080), 1,1100)
    False 
    '''
    if (coord_x >= 0 and coord_x < janela.altura) and (coord_y >= 0 and coord_y < janela.largura):
        return True 
    else: 
        return False 

def main():
    altura = int(input("Digite a altura da janela: "))
    largura = int(input("Digite a largura da janela: "))
    coord_x = int(input("Digite a coordenada x do mouse: "))
    coord_y = int(input("Digite a coordenada y do mouse: "))

    jan = Janela(altura, largura)
    
    if clicou_na_tela(jan, coord_x, coord_y):
          print("clicou")
    else:
          print("nao clicou")

#main()
