# ------------------ VIAGEM ------------------
class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0

    def set_distancia(self, d):
        self.__distancia = d

    def set_tempo(self, t):
        self.__tempo = t

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    def velocidade_media(self):
        if self.__tempo > 0:
            return self.__distancia / self.__tempo
        return 0