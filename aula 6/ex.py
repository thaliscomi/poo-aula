class Contato:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    def set_id(self, id):
        if id < 0: raise ValueError('ID deve ser positivo')
        self.__id = id
    def set_nome(self, nome):
        if nome == '': raise ValueError('nome não pode ser vazio')
        self.__nome = nome
    def set_email(self, email):self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def __str__(self): return f'{self.__id} - {self.__nome} - {self.__email} - {self.__fone}'

class ContatoUI:
    contatos = []
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()

    @staticmethod
    def menu():
        print('1-inserir 2-listar 3-atualizar 4-excluir 5-pesquisar 6-fim')
        return int(input('informe uma opção: '))
    
    @classmethod
    def inserir(cls):
        id = int(input('informe o id do contato: '))
        nome = input('informe o nome: ')
        email = input('informe o email: ')
        fone = input('informe o fone: ')
        x = Contato(id, nome, email, fone)
        cls.contatos.append(x)

    @classmethod
    def listar(cls):
        if len(cls.contatos) == 0: print('nenhum contato inserido')
        else:
            for x in cls.contatos: print(x)

ContatoUI.main()