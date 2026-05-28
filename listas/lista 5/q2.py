from enum import Enum
from datetime import datetime

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        # atributos que serão validados
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)
        # atributos com valor inicial definido
        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__sitiacao_pagamento = Pagamento.EM_ABERTO
    def set_cod_barras(self, cod):
        # supondo que o boleto deve ter 10 digitos
        if len(cod) != 10: raise ValueError('deve ter 10')
        self.__cod_barras = cod
    def set_data_emissao(self, emissao):
        if emissao > datetime.now(): raise ValueError('data de emissao não pode ser no futuro')
        self.__data_emissao = emissao
    def set__data_vencimento(self, venc):
        if venc < datetime.now(): raise ValueError('não pode ser no passado')
        self.__data_vencimento = venc
    def set_valor_boleto(self, valor):
        if valor < 0: raise ValueError('valor negativo não pode')
        self.__valor_boleto = valor
    def pagar(self, valor_pago):
        if valor_pago < 0: raise ValueError('valor não pode ser negativo')
        if self.__situacao_pagamento != Pagamento.EM.ABERTO: raise ValueError('boleto ja foi pago')
        self.__valor_pago = valor_pago
        self.__data_pagamento = datetime.now()
        if self.__valor_pago >= self.__valor_boleto: self.__situacao_pagamento = Pagamento.PAGO
    def get_cod_barras(self): return self.__cod_barras
    def get_data_emissao(self): return self.__data_emissao
    def get_data_vencimento(self): return self.__data_vencimento
    def get_data_pagamento(self): return self.__data_pagamento
    def get_valor_boleto(self): return self.__valor_boleto
    def get_valor_pago(self): return self.__valor_pago
    def get_situacao_pagamento(self): return self.__sitiacao_pagamento
    #  no diagrama get_situacao_pagamento está como situacao
    def get_situacao(self): return self.__situacao_pagamento
    def __str__(self):
        s = f"boleto: {self.__cod_barras} - Emissao: {self.__data_emissao.strftime('%d/%m/%y')}"
        s += f"vencimento: {self.__data_vencimento.strftime('%d/%m/%y')}"
        s += f"valor boleto R$ {self.__valor_boleto:.2f}"
        s += f"valor pago R$ {self.__valor_pago:.2f}"
        s += f"pagamento: {self.__data_nascimento}"
        s += f"{self.__situacao_pagamento}"
        
        return s