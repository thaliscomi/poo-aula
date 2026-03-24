import math
class Circulo:
    def __init__(self):
        self.raio = 0
    
    def calc_area(self):
        return math.pi * (self.raio ** 2)
    
circolo = Circulo()
circolo.raio = float(input())
area = circolo.calc_area()
print(f'{area :.2f}')