from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 11:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.cliente_listar_nome()
            if op == 6: UI.servico_inserir()
            if op == 7: UI.servico_listar()
            if op == 8: UI.servico_atualizar()
            if op == 9: UI.servico_excluir()
            if op == 10: UI.servico_listar_descricao()

    @staticmethod
    def menu():
        print("Clientes ----------------------------------")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir 5-pesquisa por nome")
        print("Serviços ----------------------------------")
        print("6-Inserir, 7-Listar, 8-Atualizar, 9-Excluir 10-listar por descriÇão")
        print("Outras opções -----------------------------")
        print("11-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        senha = input("Informe a senha: ")
        Service.cliente_inserir(nome, email, fone, senha)

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar(): print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service().cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service().cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def cliente_listar_nome():
        letra = input('qual nome quer procurar na lista de clientes?')
        Service.cliente_listar_nome(letra)


    @staticmethod
    def servico_inserir():
        id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(id, descricao, valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar(): print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        valor = float(input("Informe o novo valor: "))
        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser excluído: "))
        Service.servico_excluir(id)

    @staticmethod
    def servico_listar_descricao():
        letra = input('informe uma palavra pra procurar nas descrições de serviços')
        Service.servico_listar_descricao(letra)