#Algoritmo SO_Lista01.17
#Declarar.
t: float = 0;
velm: float = 0;
l: float = 0;
#Início.
t = float(input("Tempo de viagem em horas: "));
velm = float(input("Velocidade média em km/h: "));
l = velm*t/12;
print("Gasto de combustível em litros: ", l);
#FIM.