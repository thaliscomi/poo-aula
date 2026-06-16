class Conta:
    def __init__(self):
        self.nome = ""
        self.id = 0
        self.saldo = 0
    def depositar(self, valor):
        self.saldo = self.saldo + valor
    def saque(self, valor):
        self.saldo = self.saldo - valor
    
c = Conta()
c.nome = "samuel"
c.id = 7723487
c.saldo = 1000
print(c.nome)
print(c.id)
print(c.saldo)
c.depositar(344)
print(c.saldo)
c.saque(500)
print(c.saldo)