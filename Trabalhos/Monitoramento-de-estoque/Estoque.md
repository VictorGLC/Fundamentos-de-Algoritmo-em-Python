# Sistema para Empresa de Derivados de Celulose

## Contextualização

Você está atuando como desenvolvedor na equipe de TI de uma empresa que produz produtos derivados da celulose. A empresa comercializa três tipos de produtos: bobina de papel para embalagens (usados em sacolas e materiais de escritório), chapas de papelão ondulado (usados para confecção de caixas de papelão) e painéis de fibra de madeira (materiais de construção).

O gerenciamento de estoque envolve uma série de tarefas essenciais para garantir que os produtos estejam disponíveis quando necessários, evitando excessos ou faltas. Já a gestão de vendas se preocupa com a receita mensal, o lucro líquido, entre outras coisas.

A seguir estão algumas das principais atividades que precisam ser realizadas pelo sistema.

## Monitoramento de Níveis de Estoque

Refere-se ao acompanhamento constante dos níveis de estoque para garantir que eles estejam dentro dos limites adequados. Uma das preocupações da empresa é identificar possíveis casos de rupturas de estoque (quando a demanda excede o estoque disponível). Esse acompanhamento é feito mensalmente e leva em consideração a quantidade atual em estoque e a demanda dos clientes.

Sua primeira tarefa é processar os pedidos dos clientes, ou seja, dada uma lista contendo os pedidos (produto e quantidade), totalizar a demanda de cada produto. Por exemplo, para a seguinte lista de pedidos:


| Produto | Quantidade |
|---------|------------|
| Bobina  | 100        |
| Chapa   | 50         |
| Bobina  | 30         |
| Painel  | 20         |
| Chapa   | 15         |


O resultado esperado é:

| Produto | Quantidade |
|---------|------------|
| Bobina  | 147        |
| Chapa   | 65         |
| Painel  | 20         |

A equipe de TI esboçou a seguinte assinatura para a função:

```python
def totaliza_pedidos(pedidos: list[Pedido]) -> Totalizacao:
    '''
    Produz uma estrutura que totaliza a demanda de cada produto
    a partir de *pedidos*.
    '''
```

Totalizada a demanda dos produtos, desejamos saber se algum produto produzirá uma ruptura.

```python
def ha_ruptura(estoque: Totalizacao, demanda: Totalizacao) -> list[TipoProduto]:
    '''
    Gera a partir do *estoque* e *demanda*, uma lista com os tipos de produtos
    com ruptura do estoque.
    '''
```

Faça a definição dos tipos de dados e complete o projeto dessas funções.

## Vendas

O sistema de estoque está integrado com o sistema de vendas de produtos. A tabela a seguir mostra algumas informações sobre preços e disponibilidade em estoque.

| Produto   | Quantidade | Preço de custo | Preço de venda |
|-----------|------------|-----------------|-----------------|
| Papel     | 100.000    | 50,00           | 60,00           |
| Papelão   | 50.000     | 40,00           | 48,00           |
| Painéis   | 30.000     | 75,00           | 90,00           |

Embora a tabela apresente um preço de venda preestabelecido, os vendedores podem oferecer desconto aos clientes dependendo da quantidade do pedido. O preço ofertado não pode ser inferior ao preço de custo.

Assim, um dos problemas do sistema financeiro é determinar a receita mensal, visto que não basta multiplicar o total produzido pelo preço de venda. Você possui acesso ao relatório de vendas, onde cada nota de venda contém um campo indicando o nome do vendedor, o produto, a quantidade e o valor com desconto.

Projete uma função que determine a receita e o lucro líquido a partir do relatório de vendas.

A empresa costuma também premiar os três vendedores que geraram mais lucro no mês, para isso é necessário projetar uma função que determine esses três vendedores.
