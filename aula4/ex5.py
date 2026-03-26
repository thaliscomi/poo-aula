class Pais:
    def __init__(self):
        self.nome = str
        self.populacao = 0
        self.area = 0
    
    def densidade(self):
        return self.populacao / self.area
    
pais = Pais()
pais.nome = input('qual o nome do país?')
pais.populacao = int(input('qual o tamanho da populaçao?'))
pais.area = int(input('qual a area do pais?'))

print(f'a densidade demográfica do {pais.nome} é de {pais.densidade() :.2f} hab/km²')

