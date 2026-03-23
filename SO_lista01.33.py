#Algoritmo Lt01.33

#Declarar.
num : int = 0
aux : int = 2
soma : float = 1.0

#Inicio.
num = int(input("Insira um número: "))

print (soma, end="")

for aux in range (aux, (num+1), 1):
   soma += 1/aux
   print(f" + 1/{aux}", end="")

print("\n\nSoma =",soma)

#Fim.