class Circulo:
    def __init__(self):
        self.raio = 0
    def area(self):
        print(f"aproximadamente {3.14*self.raio**2}")
    def circunferencia(self):
        print(f'aproximadamente {2*3.14*self.raio}')

c = Circulo()
c.raio = 3
c.area()
c.circunferencia()