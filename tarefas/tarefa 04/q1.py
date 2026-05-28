class Time:
    def __init__(self, id, nome, estado):
        self.id = id
        self.nome = nome
        self.estado = estado
    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_estado(self):
        return self.estado
    def set_nome(self, nome):
        self.nome = nome
    def set_estado(self, estado):
        self.estado = estado
    def toString(self):
        return f"Time: {self.id} - {self.nome} ({self.estado})"

class Jogador:
    def __init__(self, id, nome, camisa, id_time):
        self.id = id
        self.nome = nome
        self.camisa = camisa
        self.id_time = id_time
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome
    def set_time(self, id_time):
        self.id_time = id_time
    def toString(self):
        return f"Jogador: {self.id} - {self.nome}, Camisa {self.camisa}, Time{self.id_time}"
#Lista de times e jogadores
class UI:
    def __init__(self):
        self.times = []
        self.jogadores = []
    def inserir_time(self):

        id = int(input("ID: "))
        nome = input("Nome: ")
        estado = input("Estado: ")
        self.times.append(Time(id, nome, estado))
    def listar_times(self):
        for t in self.times:
            print(t.toString())
    def inserir_jogador(self):
        id = int(input("ID: "))
        nome = input("Nome: ")
        camisa = int(input("Camisa: "))
        id_time = int(input("ID do time: "))
        self.jogadores.append(Jogador(id, nome, camisa, id_time))
    def listar_jogadores(self):
        for j in self.jogadores:
            print(j.toString())

    def listar_jogadores_do_time(self):
        id_time = int(input("ID do time: "))
        for j in self.jogadores:
            if j.id_time == id_time:
                print(j.toString())
    def transferir_jogador(self):
        id_jogador = int(input("ID do jogador: "))
        novo_time = int(input("Novo time: "))
        for j in self.jogadores:
            if j.id == id_jogador:
                j.set_time(novo_time)

    def menu(self):
        while True:
            print("\n1 Inserir Time")
            print("2 Listar Times")
            print("3 Inserir Jogador")
            print("4 Listar Jogadores")
            print("5 Jogadores de um Time")
            print("6 Transferir Jogador")
            print("0 Sair")
            op = input("Escolha: ")
            if op == "1":
                self.inserir_time()
            elif op == "2":
                self.listar_times()
            elif op == "3":
                self.inserir_jogador()
            elif op == "4":
                self.listar_jogadores()
            elif op == "5":

                self.listar_jogadores_do_time()
            elif op == "6":
                self.transferir_jogador()
            elif op == "0":
                break

ui = UI()
ui.menu()