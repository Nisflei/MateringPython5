import pandas as pd

print('Meu rotina para Abrir EXCEL...')

#carregando os dados
tabela_Excel = pd.read_excel('janeiro.xlsx')

print(tabela_Excel)