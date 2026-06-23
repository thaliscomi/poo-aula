from datetime import datetime 

class Contato:
    def __init__(self, id:int, nome:str, email:str, fone:str, nasc:datetime):
        self.__id(id)
        self.__nome(nome)
        self.__email(email)
        self.__fone(fone)
        self.__nasc(nasc)
    
    def set_id(self, id):
        if id < 0: raise ValueError('não pode ser negativo')
        else: self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError('não pode ser vazio')
        else: self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError('não pode ser vazio')
        else: self.__email = email
    def set_fone(self, fone):
        if fone < 0 : raise ValueError('não pode ser negativo')
        else: self.__fone = fone
    def set_nasc(self, nasc):
        if nasc > datetime.now: raise ValueError('')
        else: self.__nasc = nasc

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def get_nasc(self):
        return self.__fone

    def ToString(self):
        return f'{self.__id}, {self.__nome}, {self.__email}, {self.__fone}, {self.__nasc}'
    