#Algoritmo Lt01.44.

#Declarar.
base : int = 0.0
auxbase : int = 0.0
expoente : int = 0.0
aux : int = 0

#Iniciar.
base, expoente = map(int, input("Insira a base e o expoente, separados por espaço: ").split())
auxbase = base

if expoente == 0:
   base = 1

if expoente < 0:
   aux = 1
   expoente = -(expoente)

for cont in range(2, (expoente+1), 1):
   base *= auxbase

if aux == 1:
   base = 1 / base

print("Valor da potenciação: ", base)

#Fim.