class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def densidade(self):
        return self.populacao / self.area

    def __str__(self):
        return f"País: {self.nome}, População: {self.populacao}, Área: {self.area} km²"


class PaisUI:
    @staticmethod
    def menu():
        print("1 - Calcular")
        print("2 - Fim")
        return int(input("Escolha: "))

    @staticmethod
    def calculo():
        nome = input("Nome do país: ")
        populacao = int(input("População: "))
        area = float(input("Área (km²): "))
        
        pais = Pais(nome, populacao, area)
        
        print(pais)
        print("Densidade demográfica:", pais.densidade(), "hab/km²")

    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = PaisUI.menu()
            if op == 1:
                PaisUI.calculo()


PaisUI.main()
