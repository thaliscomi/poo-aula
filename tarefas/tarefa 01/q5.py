class Pais:
    def __init__(self):
        self.nome =""
        self.pop = 0
        self.km = 0
    def densidade(self):
        print(f'densidade no {self.nome} é de {self.pop/self.km} hab/km²')
    
p = Pais()
p.nome = "thalis"
p.pop = 213400000
p.km = 8510000
p.densidade()