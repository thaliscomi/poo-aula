# questão 2
class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area
    
    def densidade(self):
        self.d = self.populacao / self.area
        return self.d

    
dict = {}

for i in range(3):
    nome = input(f'nome pais{i+1}: ')
    populacao = float(input(f'populacao pais{i+1}: '))
    area = float(input(f'area pais{i+1}: '))

    pais = Pais(nome, populacao, area)
    pais.densidade()
    dict[pais.d] = pais.nome

print(f'o pais que apresenta a maior densidade demografica que é {max(dict)}, é o {dict[max(dict)]}')