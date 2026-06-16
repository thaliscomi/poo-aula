class Viagem:
    def __init__(self):
        self.dis = 0
        self.temp = 0
    def velocidade(self):
        print(self.dis/self.temp)

v = Viagem()
v.dis = 10
v.temp = 2
v.velocidade()