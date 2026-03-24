class Conta_bancaria:
    def __init__(self):
        self.titular = str
        self.num_conta = 0
        self.saldo = 0

    def depositar(self):
        quant = float(input('quanto você quer depositar? '))
        self.saldo += quant
        return self.saldo
    
    def sacar(self):
        quant = float(input('quanto você quer sacar? '))
        self.saldo -= quant
        return self.saldo
    
conta = Conta_bancaria()
conta.depositar()
saldo = conta.saldo
print(saldo)

conta.sacar()