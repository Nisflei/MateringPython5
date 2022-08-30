from random import randint


class Conta:
    def __init__(self,numero,digito,agencia,saldo):
        self.numero = numero
        self.digito = digito
        self._agencia = agencia
        self.saldo = saldo

    # getters / setters
    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, value):
        self._agencia = value

    # Metodos
    def dadosConta(self):
        print(f'Agencia: {self.agencia} / Num:{self.numero} /  Saldo:{self.saldo}')

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return True

    def verificarSaldo(self):
        return self.saldo

    def sacar(self, valor):
        if (self.saldo < valor):
            print(f'Saldo insuficiente para saque de  {valor}')
            return False
        self.saldo = self.saldo - valor
        return True

    @staticmethod
    def gerarNumero():
        numConta = randint(1000,1999)
        return numConta


### Criando a rotina para utilizar a Class ####

print('===== Usando ContaBancaria =======')

conta1 = Conta(1010,1,10101,850.00)
print(conta1.__dict__)

conta2 = Conta(2020,2,20202,50.01)
print(conta2.__dict__)

## Utilizando os metodos
print("---- Usando Metodos ( Objeto Conta 1)")
print(f'Deposito 100.00: {conta1.depositar(100)}')
conta1.dadosConta();
print(f'Saldo: {conta1.verificarSaldo()} ')
print(f'Saque 2000: {conta1.sacar(2000)} ')
print(f'Saldo: {conta1.verificarSaldo()} ')

print("Obter dados do cliente")

# eventos com o cliente
print(' ')
#conta2.depositar(float(input("Digite o valor de Deposito:")))
print(f'Saldo: {conta2.verificarSaldo()}')
#conta2.sacar(float(input("Digite o valor de Saque:")))
print(f'Saldo: {conta2.verificarSaldo()}')

num = Conta.gerarNumero()
print(f'numeroConta: {num}')
conta3 = Conta(num,5,1010,0)
print(conta3.__dict__)

# Alterando com Getter/Setter a agencia

conta3.agencia = 222
print(f'{conta3.agencia}')
print(conta3.__dict__)


