# Porta-Automatica

![Alt text](/porta_ex.jpg?raw=true "Porta Automática")

## Descrição

Pretende-se implementar componentes pré requisitados neste projeto (Beaglebone, comunicação CAN, controlador e motor) para confeccionar uma porta que se abrirá automaticamente na presença de uma pessoa. Seu funcionamento se dará a partir de uma determinada distância detectada pelo sensor de proximidade (ultra sônico), fazendo com que o motor rotacione em um sentido, simulando a abertura da porta. Caso a distância detectada volte à leitura padrão (inicial), o motor irá rotacionar em sentido contrário, simulando o fechamento da porta automática. Toda a comunicação do motor com a placa lógica será realizada através do protocolo CAN, bem como o envio do sinal do sensor para a placa. Além disso, o sistema também registrará os momentos em que a porta se abriu e fechou, apartir destas informações podemos obter o período que a porta permaneceu aberta e sua frequência de abertura ao longo do tempo.

## Integrantes

- Caroline Mendonça Gomes
- Fabrício Santos
- Martin Wellendorf
- Rhamy Bachour


## Requisitos funcionais

  - O sistema manterá as portas fechadas até que os sensores acusem presença.

  - O sistema deverá acionar os motores que por sua vez abrirão as portas, dado um sinal de entrada proveniente do sensor de aproximação.
  
  - O sistema monitorará as leituras dos sensores constantemente.
  
  - Após uma variação de sinal entre uma distância maior que a pré-definida para uma menor, a porta deverá permanecer em repouso durante um tempo "x3".

  - Área de leitura dos sensores devem preencher totalmente a área de travessia dos usuários.
  
  - Registrar os horários de acionamento dos motores e sentido de rotação.


## Requisitos não funcionais

  - O sensor deve detectar corretamente a presença de 95% das vezes em menos de 3 segundos.
    
  - O sistema fechará as portas após um intervalo de tempo "x1" sem mudança no sinal do sensor.
  
  - 
  
  
  ## Considerações
  
**todos os requisitos foram discutidos em conjunto, portanto todos os integrantes tiveram participação efetiva na elaboração dos requisitos: @carolinemendg & @fabriciosdsilva & @MWellen97 & @rhamybachour 


