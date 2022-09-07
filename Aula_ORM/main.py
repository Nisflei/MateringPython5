from databaseModel import  db,PetAdocao
from datetime import datetime

#limpando somente para TESTE
db.drop_all()
db.create_all()

#Simular a entrada de Dados

toto = PetAdocao('furação', 'docil', datetime.strptime('06/09/2022','%d/%m/%Y'), True, 'Ana Maria Braga','email@email')
print(f'Primeiro Registro: {toto.apelido} - {toto.responsavel}')

db.session.add(toto)
print(f'ID bando de Dados: {toto.id}')

db.session.commit()
print(f'ID bando de Dados: {toto.id} apos commit')


## Salvando lista de Dados
pets = [
    PetAdocao('Toto','nervoso, mas é brincalhao',datetime.strptime('2021-09-25','%Y-%m-%d'),False,'Nisflei','nisflei@gmail.com'),
    PetAdocao('fofinho', 'bravo', datetime.strptime('2022-09-06', '%Y-%m-%d'), True, 'Fausto Silva', 'fausto@gmail.com'),
    PetAdocao('maiau', 'docil', datetime.strptime('2022-09-06', '%Y-%m-%d'), False, 'Pedro Bial','pedro@gmail.com'),
    PetAdocao('costelinha', 'bravo', datetime.strptime('2022-09-06', '%Y-%m-%d'), False, 'Jose J', 'jj@gmail.com')
]
print(pets)

print('>> Adicionar a lista no Banco de Dados')
for pet in pets:
    db.session.add(pet)
    print(f'Salvando: {pet.id} {pet.apelido}')

db.session.commit()
for pet in pets:
    print(f'Salvando: {pet.id} {pet.apelido}')

print(pets)

#Consultando informações no BD
print()
print('>> Lendo todo os dados do Banco')
pets_db = db.session.query(PetAdocao).all()

for pet in pets_db:
    print(f'id: {pet.id} - {pet.apelido}')

#Consultar por FILTRO registro no Banco de Dados
pet_consulta = PetAdocao.query.filter_by(perfil='docil').all()
print(f'Achou:{pet_consulta}')

#Consultar por FILTRO de 1 registro no Banco de Dados
pet_consulta = PetAdocao.query.filter_by(id=5).first()
print(f'Buscando id=5 : {pet_consulta.id} - {pet_consulta.apelido} - {pet_consulta.contato}')

#Removendo esse registro
db.session.delete(pet_consulta)
db.session.commit()

# UPDATE dos dados
# Objeto não transient ja esta relacionado ao banco.
toto.responsavel = 'Fausto Silva'
db.session.commit()
