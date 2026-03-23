#Algoritmo Lt01_27.

#Declarar.
voltas : float = 0
metros : float = 0
tempo : float = 0
vel_md : float = 0

#Iniciar.
voltas, metros, tempo = map(float, input("Insira o número de voltas, extensão do circuito (em metros), e tempo (em minutos), separados por espaço: ").split())

voltas = voltas*metros/1000
tempo = tempo/60
vel_md = voltas/tempo

print("Velocidade média do percurso: ",vel_md,"km/h")

#Fim.