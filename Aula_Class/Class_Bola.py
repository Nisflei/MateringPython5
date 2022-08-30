from Class_ContaBancaria import Conta

class Bola:
    def __init__(self, material, formato, tamanho, nomeDaCor, tipoDeMontagem, segmento):
        self.material = material
        self.formato = formato
        self.tamanho = tamanho
        self.cor = nomeDaCor
        self.tipoDeMontagem = tipoDeMontagem
        self.tamanhoSegmento = segmento
        self.valor = None

print("+++++++ Usando a Classe +++++++++")

#construtor Bola
futebol = Bola('couro', 'redonda', '40 cm', 'branca','costura', 'intercalo Preto')
ping_pong = Bola('plastico','redonda','1.5 cm','bege','','')

futebol.valor = 100
print(f'Objeto: Futebol - {futebol.material} / {futebol.cor}')
print(futebol.__dict__)
print(ping_pong.__dict__)

contaX = Conta(1,1,1,0)
print(f' contaX Saque: {contaX.sacar(10000)}')
print(f' contaX Saldo: {contaX.verificarSaldo()}')