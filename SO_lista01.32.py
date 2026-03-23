#Algoritmo Lt01.32.

#Declarar.
num : int = 0
aux : int = 0
fatorial : int = 1

#Inicio.
num = int(input("Insira o valor para cálculo de fatorial: "))

for aux in range (1, (num+1)):
   fatorial *= aux

print("Valor do fatorial: ", fatorial)

#Fim.