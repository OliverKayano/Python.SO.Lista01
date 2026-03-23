# Algoritmo Lt01.45.

#Declarar.
soma : float = 1.0

#Inicio.
print(soma, end="")

for cont in range(2, 16, 1):

   if (cont % 2 == 0):
      soma -= cont/(cont*cont)
      print(f" - {cont}/{cont*cont}", end="")

   else:
      soma += cont/(cont*cont)
      print(f" + {cont}/{cont*cont}", end="")

print("\n\nSoma =", soma)

#Fim.