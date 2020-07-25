# Porta-Automatica

![Alt text](/porta_ex.jpg?raw=true "Porta Automática")

## Motivação

O momento de insegurança e medo que o novo coronavírus trouxe aos anos de 2019 e 2020 fez com que grande parte da população mundial começasse a prestar mais atenção em algumas atitudes que antes passavam despercebidas, como a lavagem correta das mãos, alimentação mais saudável e contato com superfícies públicas sem proteção. Levando isso em consideração, surge a grande motivação de criar um sistema para uma porta automática, na qual não seria necessário tocar em uma maçaneta sem as proteções adequadas, uma simples aproximação é suficiente para adentrar e sair do local.

## Descrição

Pretende-se implementar componentes pré requisitados neste projeto (Beaglebone, comunicação CAN, controlador e motor) para confeccionar uma porta que se abrirá automaticamente na presença de uma pessoa. Seu funcionamento se dará a partir de uma determinada distância detectada pelo sensor de proximidade (ultra sônico), fazendo com que o motor rotacione em um sentido, simulando a abertura da porta. Caso a distância detectada volte à leitura padrão (inicial), o motor irá rotacionar em sentido contrário, simulando o fechamento da porta automática. Toda a comunicação do motor com a placa lógica será realizada através do protocolo CAN, bem como o envio do sinal do sensor para a placa. Além disso, o sistema também registrará os momentos em que a porta se abriu e fechou, apartir destas informações podemos obter o período que a porta permaneceu aberta e sua frequência de abertura ao longo do tempo.
Projeto desenvolvido para a discplina de Sistemas Embarcados (SEM0544, 1o semestre de 2020) do Curso de Engenharia Mecatrônica EESC-USP.

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
  
   ## Como faremos para contemplar os requisitos
 
 - O sistema fará constante leitura dos sensores para garantir a correta detecção de pessoas, e consequentemente o devido acionamento dos motores para abertura da porta, e também fechá-la conforme as condições especificadas;
 
 - Para cumprir as especificações de desempenho mostradas (tempo de resposta e recorrência de falhas), a porta contará com mecanismo de fácil movimentação, oferencendo a menor restencia possível, dentro de um bom custo benefício. Além disso, utilizaremos motores que forneçam uma resposta adequada ao comportamento desejado.
 
 - A grande maioria das portas automáticas comerciais têm mecanismo composto por motor, atuador e correia dentada para transmissão do movimento. O grupo realizaria a confecção do protótipo seguindo a mesma ideia, uma vez se trata de uma solução barata e eficiente para o sistema.
  
 ## Simulação 
 
 O projeto sofreu algumas alterações em relação ao desenvolvimento, devido a Pandamia do Covid-19, a construção física do projeto não pode ser executada e portanto o projeto se limitou a algumas simulações. Assim, desenvolveu-se uma aplicação em Python simulando o cenário de controle e automação das portas. Na imagem abaixo é mostrado um trecho das simulações realizadas. A simulação foi executada durante 100 segundos.



Apesar de ser apenas uma simualçao, o algoritimo já esta estruturado para receber as conexões físicas do hardware, necessitando de poucos ajustes para ser aplicado ao controle dos motores e sensores da porta. Além disso, a estrutura no qual o algoritimo foi escrito permite o registro e controle de N portas. Também é possível registrar, por exemplo, o fluxo de pessoas, o tempo em que a porta permaneceu aberto durante todo o tempo, etc.

  ## Considerações
  
  - Com o requisito de leitura de horário e sentido de rotação dos motores, buscamos fornecer informações a cerca do uso da porta, permitindo a obtenção de dados tais como: Tempo que a porta permanceu aberta e fechada em determinado horário do dia; quantidade de vezes que a porta foi aberta; mensurar movimentação de pessoas no ambiente durante um período pré definido. Tudo isso permitirá análises de diversos tipos, beneficiando o estabelecimento que fizer uso do produto. Facilitando a tomada de decisão a cerca do sistema de refrigeração, circulação de pessoas no ambiente em diferentes épocas do ano. E no caso de mais de uma porta instalada, para o caso dos shoppings por exemplo, verificar qual área do shopping tem sido mais acionada. 
  
**todos os requisitos foram discutidos em conjunto, portanto todos os integrantes tiveram participação efetiva na elaboração dos requisitos: @carolinemendg & @fabriciosdsilva & @MWellen97 & @rhamybachour 


