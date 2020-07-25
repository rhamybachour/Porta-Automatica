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

    def __init__(self, calendario, motorEsquerdo, motorDireito, sensorEntrada, sensorSaida):
        self.calendario = calendario
        self.sensorPortaEntrada = sensorSaida
        self.sensorPortaSaida = sensorEntrada
        self.motorPortaEsquerda = motorEsquerdo
        self.motorPortaDireita = motorDireito
        
        #Fechada = False / Aberta = True
        self.__estadoPorta = False
        
        #Tempo em segundos
        self.__tempoEsperaPorta = 5
        self.__tempoAberturaPorta = 3
        self.__tempoFechamentoPorta = 3
        

    def detectaPessoa(self):

        #Se os sensores detectaram pessoas saindo ou entrando
        if self.sensorPortaEntrada.getEstado() == True or self.sensorPortaSaida.getEstado() == True:

            #Verifica se a porta esta fechada
            if self.__estadoPorta == False:
                self.abrePorta()

            #Verifica se não chega outra pessoa durante o tempo de espera   
            self.aguardaPorta()

            #Atualiza os sensores
            if self.sensorPortaEntrada.getEstado() == True:
                self.sensorPortaEntrada.setEstado(False)

            if self.sensorPortaSaida.getEstado() == True:
                self.sensorPortaSaida.setEstado(False)
                
    def aguardaPorta(self):

        tempo = 0
        tempoExtra = 0
        
        #Avança o tempo com a porta aberta    
        print(Cores.YELLOW + "[%d] AGUARDANDO SENSORES" % calendario.getTempoReal(), end = '')
        time.sleep(1)
        print(".", end = '')        
        time.sleep(0.5)
        print(".", end = '')        
        time.sleep(0.5)
        print(".\n\n")
        time.sleep(1)

        #Gera a chegada de uma pessoa durante o tempo de espera de forma aleatória
        while tempo < self.__tempoEsperaPorta + tempoExtra:
            #Probabilidade de outra pessoa passar na porta a cada segundo
            if random.randint(1,20) == 1:
                tempoExtra = tempo
                self.calendario.setTempoReal(calendario.getTempoReal() + tempo)
                
                print(Cores.YELLOW + "[%d] OPA CHEGOU OUTRA PESSOA!" % calendario.getTempoReal())
                print(Cores.YELLOW + "[%d] AGUARDANDO SENSORES" % calendario.getTempoReal(), end = '')
                time.sleep(1)
                print(".", end = '')        
                time.sleep(0.5)
                print(".", end = '')        
                time.sleep(0.5)
                print(".\n\n")
                time.sleep(1)


            tempo += 1

        #Atualiza o tempo total decorrido
        self.calendario.setTempoReal(calendario.getTempoReal() + self.__tempoEsperaPorta)


    def verificaPessoa(self):
        
        #Verifica se ainda há presença de pessoas na porta
        if self.sensorPortaEntrada.getEstado() == False and self.sensorPortaSaida.getEstado()  == False:

        #Verifica se a porta esta aberta
            if self.__estadoPorta == True:
                self.fechaPorta()
	
    def abrePorta(self):	
		pass
	
    def fechaPorta(self):
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
