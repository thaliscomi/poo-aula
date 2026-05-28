class Viagem:
    def __init__(self):
        self.km = 0
        self.tempo = 0

    def calc_velocidade(self):
        return self.km // self.tempo

viagem = Viagem()   
viagem.km = float(input('coloque a distancia em km: '))
viagem.tempo = float(input('coloque o tempo gasto em horas: '))
velocidade = viagem.calc_velocidade()
print(f'nessa viagem, a velocidade foi de {velocidade}km/h')