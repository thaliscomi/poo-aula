from datetime import datetime, timedelta
class Treino:
    def __init__(self, id=int, data=datetime, distancia=float, tempo=timedelta):
        self.__id(id)
        self.__data(data)
        self.__distancia(distancia)
        self.__tempo(tempo)

    def set_id(self, id):
        if id<0: raise ValueError('id não pode ser negativo')
        else: self.__id = id
    def set_data(self, data):
        if datetime.now < data: raise ValueError('não pode ser no futuro')
        else: self.__data= data
    def set_distancia(self, distancia):
        if distancia < 0: raise ValueError('distancia não pode ser negativa')
        else: self.__distancia = distancia
    def set_tempo(self, tempo):
        if tempo < timedelta(0): raise ValueError('vai voltar no tempo é? ajeita esse negócio logo')
        else: self.__tempo = tempo

    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_distanica(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    
    def pace(self):
        segundos = self.__tempo.total_seconds()
        pace_segundos = segundos / self.__distancia

        minutos = int(pace_segundos // 60)
        segundos_restantes = int(pace_segundos % 60)

        return f'{minutos}min {segundos_restantes}s por km'