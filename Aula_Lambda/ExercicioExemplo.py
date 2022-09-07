produtos = [
    {'Produto': 'MILHO',  'Frete': 0.90, 'Origem': 'MT', 'Destino': 'SP', 'Peso_kg': 5500.0},
    {'Produto': 'SOJA',   'Frete': 0.55, 'Peso_kg': 4300.0, 'Origem': 'MS', 'Destino': 'SP'},
    {'Produto': 'ALGODÃO','Frete': 0.13, 'Peso_kg': 3000.0, 'Origem': 'GO', 'Destino': 'MT'},
    {'Produto': 'MILHO',  'Frete': 0.49, 'Peso_kg': 8000.0, 'Origem': 'MS', 'Destino': 'MT'},
    {'Produto': 'MILHO',  'Frete': 0.22, 'Peso_kg': 5000.0, 'Origem': 'MS', 'Destino': 'MT'},
    {'Produto': 'ADUBO',  'Frete': 0.79, 'Peso_kg': 4500.0, 'Origem': 'SP', 'Destino': 'MS'},
    {'Produto': 'SOJA',   'Frete': 0.31, 'Peso_kg': 8000.0, 'Origem': 'GO', 'Destino': 'SP'},
    {'Produto': 'RAÇÃO',  'Frete': 0.27, 'Peso_kg': 1500.0, 'Origem': 'SP', 'Destino': 'MS'},
    {'Produto': 'ARROZ',  'Frete': 1.90, 'Peso_kg': 5300.0, 'Origem': 'RS', 'Destino': 'PR'},
]

print(produtos)
#1 Colocar em order de peso_kg

produtos.sort(key=lambda elemento: elemento['Peso_kg'])
print(f'Produto ordenado por peso: {produtos}')

#1 Colocar em order Origem + produto
produtos.sort(key=lambda elemento: elemento['Origem'] and elemento['Produto'])
print(f'Produto ordenado por Produto+Origem: {produtos}')

#2 Vamos extrais somente a lista de preço
precos = list(map(lambda elemento: elemento['Frete'], produtos))
print(precos)

#3 Devido ao combustivel, reajustar em 10% o frete
precos = list(map(lambda elemento: round(elemento * 1.10,2),precos))
print(precos)

#USANDO listcomprehension
preco = [round(elemento * 1.10,2) for elemento in precos]
print(f'listcomprehension:{preco}')

# Reajustar os valores na TABELA DE PRODUTOS
def calcular(valor):
    return round(valor * 1.10,2)

novaListaProdutos = list(map(lambda elemento: {**elemento, 'Frete': calcular(elemento['Frete']) },produtos))
print(novaListaProdutos)

#USANDO listcomprehension
novaListaProdutosCompre = [{**elemento, 'Frete': calcular(elemento['Frete'])} for elemento in produtos]
print(f'novaListaProdutosCompre:{novaListaProdutosCompre}')

#USANDO listcomprehension CRIAR NOVA LISTA com milho para RS
novaMilhoRS = [{**elemento, 'Destino': 'RS'} for elemento in produtos if elemento['Produto'] == 'MILHO']
print(f'novaMilhoRS:{novaMilhoRS}')

#USANDO listcomprehension MESMA LISTA com milho para RS
atualMilhoRS = [{**elemento, 'Destino': 'RS'} if elemento['Produto'] == 'MILHO' else elemento for elemento in produtos]
print(f'atualMilhoRS:{atualMilhoRS}')



#4 Temos que transporta MILHO, sendo assim gerar uma nova Lista
print('ex4')
produto_milho = list(filter(lambda elemento: elemento['Produto'] == 'MILHO', novaListaProdutos))
print(produto_milho)

#5 Apresente o valor Total (milho e soja) considerando frete * peso

#filtrar milho e soja
print('ex5')
soja_milho = list(filter(lambda elemento: elemento['Produto'] == 'MILHO' or  elemento['Produto'] == 'SOJA', novaListaProdutos))
print(soja_milho)


from functools import reduce

# --- precisa resolver esse problema... dica usar MAP ou veja os parametros do REDUCE (documentação)

#TotalSoja_milho = reduce(lambda soma, elemento : soma + (elemento['Frete'] * elemento['Peso_kg']), soja_milho)
#solução:
TotalSoja_milho = reduce(lambda soma, elemento : soma + (elemento['Frete'] * elemento['Peso_kg']), soja_milho,0)
print(f'Total do Valor: {TotalSoja_milho}')