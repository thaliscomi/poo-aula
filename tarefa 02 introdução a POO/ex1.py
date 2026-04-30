# questão 1
class Agua:
    def __init__(self):
        self.mes = 0
        self.ano = 0
        self.consumo = 0

    def calc_conta(self):
        if self.consumo <= 10:
            valor = 38
        elif self.consumo <= 20:
            valor = self.consumo * 5 + 38
        else:
            valor = self.consumo * 5 + 38 + self.consumo * 6
        
        return valor

conta = Agua()
conta.consumo = int(input())
valor = conta.calc_conta()
print(valor)