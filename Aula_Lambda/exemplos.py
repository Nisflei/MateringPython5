
print('aula Lambda')

print('Calculando imposto ICMS:')

#montar um função
def calculo_ICMS(valor):
    return valor * 0.18

print('Valor de imposto para R$ 100.00')
print(f'R$ {calculo_ICMS(100.00)}')

#solução com Lambda ( sem precisar de Função )
calculo_ICMS2 = lambda valor: valor * 0.18
print(f'R$ {calculo_ICMS2(100.00)}')

# Exemplo 2 : Lambda + Função
def calculo_imp(imposto):
    return lambda valor: valor * imposto

icms_sp = calculo_imp(0.18)
icms_rj = calculo_imp(0.12)
print(f'Imposto ICMS-SP para R$ 100.00 : {icms_sp(100.00)}')
print(f'Imposto ICMS-RJ para R$ 100.00 : {icms_rj(100.00)}')
print(icms_sp)

# Usando SORT

lista= [['Prod1',100],
        ['Prod5',500],
        ['Prod2',200],
        ['Prod4',400]]

print(lista)
print("-- Order na Lista:")
def func_Ordenar(linha):
    return linha[1]

lista.sort(key=func_Ordenar)
print(lista)

print("-- Order na Lista (lambda):")
lista2= [['Prod1',100],
        ['Prod5',500],
        ['Prod2',200],
        ['Prod4',400]]
lista2.sort(key=lambda linha: linha[1])
print(lista2)

# Calculando valores com MAP
print("-- Usando o MAP")
lista_valores = [100, 500, 400]
novosValores = list(map(lambda x: x*2,lista_valores ))
print(novosValores)

#Usando Texto
animais = ["cao",
           "gato",
           "coelho",
           "papagaio"]

# o texto inteiro na linha
lista_animais = list(map( lambda texto:str.upper(texto), animais ))
#parte da string do texto
lista_animais = list(map( lambda linha: str.upper(linha[1]), animais))

print(lista_animais)

# Usando Filter (filtrar para novos grupos)
print("-- Filter :")
lista= [['Prod1',100],
        ['Prod5',500],
        ['Prod2',200],
        ['Prod4',400]]

listaFilter = list(filter(lambda linha: linha[1] >=300, lista))
print(listaFilter)

# Usando REDUCE
from functools import reduce
listanumero = [ 2, 3, 4 ,5 ,6]
valorTotal = reduce(lambda acumulado, item: acumulado + item, listanumero)
print(f'Aplicando Reduce: {listanumero} - valor Somatorio: {valorTotal}')



print('')
lista= [['Prod1',100],
        ['Prod5',500],
        ['Prod2',200],
        ['Prod4',400]]

somenteValor = list(map(lambda linha: linha[1],lista))
print(somenteValor)
total = reduce(lambda acumulado, item: acumulado + item, somenteValor)
print(f'SomenteValores: {somenteValor} - total:{total}')