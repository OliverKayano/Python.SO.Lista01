#Algoritmo Lt01.42.

#Declarar.
aux : int = 1
soma : float = 1

#Inicio.
print("\n",soma, end="")

for cont in range (2, 51, 1):
   aux += 2
   soma += cont/aux
   print(f" + {cont}/{aux}", end="")

print("\n\nSoma = ",soma)

#Fim.