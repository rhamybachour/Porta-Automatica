import random
import time


class Cores:
    """
    Classe responsável pela coloração do texto
    """
    
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'

class Calendario:
    """
    Classe responsável pela definição do objeto calendario
    """

    def __init__(self):
        self.__tempo_real = 0

    def getTempoReal(self):
        return self.__tempo_real

    def setTempoReal(self, tempoReal):
        self.__tempo_real = tempoReal

    def geraPessoa(self):
        return random.randint(1,5)


class Motor:
    """
    Classe responsável pela definição do objeto motor
    """

    def __init__(self):
        #Parado = False / Em funcionamento = True
        self.__estado = False
        
        #Fechado = False / Aberto = True
        self.__posicao = False


    def setEstado(self, estado):
        self.__estado = estado


    def getEstado(self):
        return self.__estado


    def setPosicao(self, posicao):
        self.__posicao = posicao


    def getPosicao(self):
        return self.__posicao

class Sensor:
    """
    Classe responsável pela definição do objeto sensor
    """

    def __init__(self):
        #Sem presença = False / Presença = True
        self.__estado = False


    def setEstado(self, estado):
        self.__estado = estado


    def getEstado(self):
        return self.__estado

class Porta:
    """
    Classe responsável pela definição do objeto porta
    """

    pass


################## Simulação ###############################
if __name__ == '__main__':

	#Alocação dos objetos que compõem a porta
	calendario = Calendario()
	sensor_entrada = Sensor()
	sensor_saida = Sensor()
	motor_esquerdo = Motor()
	motor_direito = Motor()
	porta = Porta(calendario, motor_esquerdo, motor_direito, sensor_entrada, sensor_saida)
