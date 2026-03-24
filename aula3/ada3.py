class Triangulo:
    def __init__(self):
        self.h = 0
        self.b = 0
    
    def calc_area(self):
        return self.b * self.h / 2
    
x = Triangulo()
x.b = 10
x.h = 20
y = x
y.b = 30
y.h = 40
x.h = 23
print(x.b, x.h)