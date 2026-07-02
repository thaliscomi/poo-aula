from service import Service
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            elif op == 2: UI.cliente_inserir()
            elif op == 3: UI.cliente_atualizar()
            elif op == 4: UI.cliente_excluir()
            