class Triangulo:
    def __init__(self):
        self.h = 0
        self.b = 0
    
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo()
x.b = float(input())
x.h = float(input())
a = x.calc_area()
print(f'{a}')

