import random
import time

class Calendario:
    """
    Classe responsável pela definição do objeto calendario
    """
    pass


class Motor:
    """
    Classe responsável pela definição do objeto motor
    """

	pass

class Sensor:
    """
    Classe responsável pela definição do objeto sensor
    """

    pass

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