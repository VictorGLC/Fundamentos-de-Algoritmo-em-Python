from dataclasses import dataclass
from enum import Enum,auto

### Monitoramento de estoque ###
@dataclass
class Pedido:
    '''
    Será uma lista de produtos com as suas determinadas quantidades (bobina,chapa e painel).
    '''
    nome: str
    quantidade: int
    valor: float

class TipoProduto(Enum):
    BOBINA = auto()
    CHAPA = auto()
    PAINEL = auto()

@dataclass
class Totalizacao:
    '''
    Vai pegar a lista dos produtos do pedido e vai totalizar as quantidades dos produtos
    (bobina, chapa e painel) nesta classe.
    '''
    nome: list
    quantidade: list

def ordem_alfabetica_nomes_produto(lista: list[Pedido]) -> list:
    '''
    Recebe uma lista de pedidos e retorna uma lista com o nome desses pedidos de forma ordenada alfabeticamente.
    Exemplos:
    >>> ordem_alfabetica_nomes_produto([Pedido('Bobina',100,60.0),Pedido('Chapa',50,48.0),Pedido('Bobina',30,60.0),Pedido('Painel',20,90.0),Pedido('Chapa',15,48.0),Pedido('Bobina',17,60.0)])
    ['Bobina', 'Chapa', 'Painel']
    '''
    lista_alfabetica = []
    
    for i in range(len(lista)):
        if not lista[i].nome in lista_alfabetica:
            lista_alfabetica.append(lista[i].nome)

    lista_alfabetica.sort()
    return lista_alfabetica

def totaliza_pedidos(pedidos: list[Pedido]) -> Totalizacao:
    '''
    Produz uma estrutura que totaliza a demanda de cada produto
    a partir de *pedidos*.
    Exemplos:
    >>> totaliza_pedidos([Pedido('Bobina',100,60.0),Pedido('Chapa',50,48.0),Pedido('Bobina',30,48.0),Pedido('Painel',20,90.0),Pedido('Chapa',15,48.0),Pedido('Bobina',17,60.0)])
    Totalizacao(nome=['Bobina', 'Chapa', 'Painel'], quantidade=[147, 65, 20])
    >>> totaliza_pedidos([Pedido('Bobina',20,60.0),Pedido('Bobina',40,60.0),Pedido('Chapa',50,48.0),Pedido('Painel',80,90.0),Pedido('Chapa',20,48.0)])
    Totalizacao(nome=['Bobina', 'Chapa', 'Painel'], quantidade=[60, 70, 80])
    '''
    nome_pedidos: list = ordem_alfabetica_nomes_produto(pedidos)
    quantidade_pedidos: list = []
    soma_pedidos:int = 0

    for i in range(len(nome_pedidos)):
        for j in range(len(pedidos)):
            if nome_pedidos[i] == pedidos[j].nome:
                soma_pedidos = soma_pedidos + pedidos[j].quantidade
        quantidade_pedidos.append(soma_pedidos)
        soma_pedidos=0
    

    totalizacao: Totalizacao = Totalizacao(nome_pedidos, quantidade_pedidos)
    return totalizacao

def ha_ruptura(estoque: Totalizacao, demanda: Totalizacao) -> list[TipoProduto]:
    '''
    Gera a partir do *estoque* e *demanda*, uma lista com os tipos de produtos
    com ruptura do estoque.
    >>> ha_ruptura(Totalizacao(['bobina','painel','chapa'],[80,70,100]),Totalizacao(['bobina','painel','chapa'],[90,80,130]))
    [<TipoProduto.BOBINA: 1>, <TipoProduto.PAINEL: 3>, <TipoProduto.CHAPA: 2>]
    >>> ha_ruptura(Totalizacao(['bobina','chapa','painel'],[80,70,100]),Totalizacao(['bobina','chapa','painel'],[60,70,130]))
    [<TipoProduto.PAINEL: 3>]
    >>> ha_ruptura(Totalizacao(['bobina','chapa','painel'],[80,70,100]),Totalizacao(['bobina','chapa','painel'],[60,70,30]))
    []
    '''

    rupturas: list[TipoProduto] = []
    tipo_enum: TipoProduto

    for i in range(len(estoque.nome)):
        if estoque.quantidade[i] < demanda.quantidade[i]:
            if estoque.nome[i].upper() == TipoProduto.BOBINA.name:
                tipo_enum = TipoProduto.BOBINA
            elif estoque.nome[i].upper() == TipoProduto.CHAPA.name:
                tipo_enum = TipoProduto.CHAPA
            elif estoque.nome[i].upper() == TipoProduto.PAINEL.name: 
                tipo_enum = TipoProduto.PAINEL
            else:
                return rupturas

            rupturas.append(tipo_enum)

    return rupturas

### Vendas ###
@dataclass
class Vendedor:
    nome: str
    lucro: float

@dataclass
class NotasDeVenda:
	vendedor: Vendedor
	pedido: Pedido
	dar_desconto: bool

@dataclass
class Receita:
    lucro_bruto: float
    lucro_liquido: float
    lucro_bobinas: float
    lucro_chapas: float
    lucro_paineis: float
    desconto_total: float

def calcular_desconto(pedido: Pedido) -> float:
    '''
    Gera a partir de *pedido* um desconto baseado na quantidade de itens do produto.
    Os descontos serão definidos da seguinte forma: para 500 unidades será ofertado desconto de 2%,
    para 1000 unidades desconto de 3%, 5000 unidades 5%, e para mais de 10000 unidades será 
    ofertado um desconto de 7%.
    >>> calcular_desconto(Pedido('Bobina',10000,60.0))
    558000.0
    >>> calcular_desconto(Pedido('Painel',500,90.0))
    44100.0
    '''
    desconto: float
    valor_total = pedido.valor * pedido.quantidade

    if pedido.quantidade >= 10000:
        desconto = 0.07
    elif pedido.quantidade >= 5000:
        desconto = 0.05
    elif pedido.quantidade >= 1000:
        desconto = 0.03
    elif pedido.quantidade >= 500:
        desconto = 0.02
    else:
        return valor_total

    return valor_total - (valor_total * desconto)

def calcular_lucro_bruto(notas_de_venda: list[NotasDeVenda]) -> float:
    '''
    Recebe *notas_de_venda* e calcula o lucro bruto de todas as notas de venda.
    Exemplo:
    >>> calcular_lucro_bruto([NotasDeVenda(Vendedor('roberto',5000.0),Pedido('Bobina',600,60.0),True), NotasDeVenda(Vendedor('José',10000.0), Pedido('Chapa',1000,48.0), False), NotasDeVenda(Vendedor('Fabio',8000.0), Pedido('Painel',3000, 90.0), True)])
    345180.0
    '''
    lucro: float = 0
    for i in range(len(notas_de_venda)):
        if notas_de_venda[i].dar_desconto:
            lucro = lucro + calcular_desconto(notas_de_venda[i].pedido)
        else:
            lucro = lucro + (notas_de_venda[i].pedido.quantidade * notas_de_venda[i].pedido.valor)
    
    return lucro

def calcular_lucro_liquido_total(notas_de_venda: list[NotasDeVenda]) -> float:
    '''
    Recebe *notas_de_venda* e calcula o lucro liquido de todas as notas de venda/pedidos.
    Exemplo:
    >>> calcular_lucro_liquido_total([NotasDeVenda(Vendedor('roberto',5000.0),Pedido('Bobina',600,60.0),True), NotasDeVenda(Vendedor('José',10000.0), Pedido('Chapa',1000,48.0), False), NotasDeVenda(Vendedor('Fabio',8000.0), Pedido('Painel',3000, 90.0), True)])
    57530.0
    '''
    lucro: float = 0.
    for i in range(len(notas_de_venda)):
        if notas_de_venda[i].pedido.nome.lower() == 'bobina':
            notas_de_venda[i].pedido.valor = 10
        elif notas_de_venda[i].pedido.nome.lower() == 'chapa':
            notas_de_venda[i].pedido.valor = 8
        elif notas_de_venda[i].pedido.nome.lower() == 'painel':
            notas_de_venda[i].pedido.valor = 15
        else:
            return notas_de_venda[i].pedido.valor
            
        if notas_de_venda[i].dar_desconto:
            lucro = lucro + calcular_desconto(notas_de_venda[i].pedido)
        else: 
            lucro = lucro + (notas_de_venda[i].pedido.quantidade * notas_de_venda[i].pedido.valor)

    return lucro

def calcular_lucro_liquido_pedidos(notas_de_venda: NotasDeVenda) -> float:
    '''
    Recebe *notas_de_venda* e calcula o lucro liquido do pedido que está na nota de venda.
    Exemplo:
    >>> calcular_lucro_liquido_pedidos(NotasDeVenda(Vendedor('roberto',5000.0),Pedido('Bobina',600,60.0),True))
    5880.0
    '''
    lucro: float = 0.
    if notas_de_venda.pedido.nome.upper() == TipoProduto.BOBINA.name:
        notas_de_venda.pedido.valor = 10
    elif notas_de_venda.pedido.nome.upper() == TipoProduto.CHAPA.name:
        notas_de_venda.pedido.valor = 8
    elif notas_de_venda.pedido.nome.upper() == TipoProduto.PAINEL.name:
        notas_de_venda.pedido.valor = 15
    else:
        return notas_de_venda.pedido.valor
        
    if notas_de_venda.dar_desconto:
        lucro = lucro + calcular_desconto(notas_de_venda.pedido)
    else: 
        lucro = lucro + (notas_de_venda.pedido.quantidade * notas_de_venda.pedido.valor)

    return lucro
    
def receita_mensal(notas_de_venda: list[NotasDeVenda]) -> Receita:
    '''
    Gera a partir de *notas_de_venda* um relatório com a receita contendo o lucro bruto,
    lucro liquido, lucro liquido de cada produto e o valor do desconto total obtido de cada pedido.
    Como tambem, atualiza o lucro do vendedor adicionando o valor liquido do pedido
    que ele obteve na venda do produto. 
    Exemplo:
    >>> receita_mensal([NotasDeVenda(Vendedor('roberto',5000.0),Pedido('Bobina',600,60.0),True), NotasDeVenda(Vendedor('José',10000.0), Pedido('Chapa',1000,48.0), False), NotasDeVenda(Vendedor('Fabio',8000.0), Pedido('Painel',3000, 90.0), True)])
    Receita(lucro_bruto=345180.0, lucro_liquido=57530.0, lucro_bobinas=5880.0, lucro_chapas=8000.0, lucro_paineis=43650.0, desconto_total=1470.0)
    '''
    receita: Receita = Receita(0,0,0,0,0,0)
    
    receita.lucro_bruto = calcular_lucro_bruto(notas_de_venda)
    receita.lucro_liquido = calcular_lucro_liquido_total(notas_de_venda)

    # percorre todas as notas de venda e verifica os pedidos, com base no nome do pedido é calculado o lucro liquido do produto
    for i in range(len(notas_de_venda)):
        if notas_de_venda[i].pedido.nome.lower() == 'bobina':
            receita.lucro_bobinas = receita.lucro_bobinas + calcular_lucro_liquido_pedidos(notas_de_venda[i])
        elif notas_de_venda[i].pedido.nome.lower() == 'chapa':
            receita.lucro_chapas = receita.lucro_chapas + calcular_lucro_liquido_pedidos(notas_de_venda[i])
        elif notas_de_venda[i].pedido.nome.lower() == 'painel':
            receita.lucro_paineis = receita.lucro_paineis + calcular_lucro_liquido_pedidos(notas_de_venda[i])
        else:
            return
        
        # calculando o valor total do desconto de todas as notas de venda
        if notas_de_venda[i].dar_desconto:
            receita.desconto_total = receita.desconto_total + ((notas_de_venda[i].pedido.valor*notas_de_venda[i].pedido.quantidade) - calcular_desconto(notas_de_venda[i].pedido))

        # nesta linha adicionamos no tipo composto do vendedor o lucro liquido do pedido que ele obteu para a empresa. 
        # como o lucro do vendedor foi atualizado dentro da funcao, apos chamarmos esses mesmos vendedores fora da funcao
        # seus lucros estarao atualizados 
        notas_de_venda[i].vendedor.lucro = notas_de_venda[i].vendedor.lucro + (notas_de_venda[i].pedido.valor * notas_de_venda[i].pedido.quantidade)

    return receita

def vendedor_maior_lucro(vendedores: list[Vendedor]) -> Vendedor:
    '''
    Esta função recebe uma lista de vendedores e retorna qual destes vendedores possui
    o maior lucro dentre eles.
    Exemplo:
    >>> vendedor_maior_lucro([Vendedor('Alfredo',4000.0),Vendedor('José',7000.0),Vendedor('Bernardo',10000.0), Vendedor('Victor',12000.0), Vendedor('Godofredo',5000.0)])
    Vendedor(nome='Victor', lucro=12000.0)
    '''
    maior: float = vendedores[0].lucro
    maior_vendedor: Vendedor = vendedores[0]

    for i in range(len(vendedores)):
        if vendedores[i].lucro > maior:
            maior = vendedores[i].lucro
            maior_vendedor = vendedores[i]

    return maior_vendedor

def premiacao_vendedores(vendedores: list[Vendedor]) -> list[Vendedor]:
    '''
    A partir de *vendedores* é retornado os 3 vendedores com o maior lucro no mês.
    Exemplos:
    >>> premiacao_vendedores([Vendedor('Alfredo',4000.0),Vendedor('José',7000.0),Vendedor('Bernardo',10000.0), Vendedor('Victor',12000.0), Vendedor('Godofredo',5000.0)])
    [Vendedor(nome='Victor', lucro=12000.0), Vendedor(nome='Bernardo', lucro=10000.0), Vendedor(nome='José', lucro=7000.0)]
    '''
    ganhadores: list[Vendedor] = []

    for i in range(3):
        maior_vendedor = vendedor_maior_lucro(vendedores)
        
        ganhadores.append(maior_vendedor)
        vendedores.remove(maior_vendedor)

    return ganhadores