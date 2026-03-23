#Algoritmo Lt01.39.

#Declarar.
grãos : int = 0
soma : int = 0

#Inicio.

for cont in range(1, 65, 1):
   grãos = 2**(cont - 1)
   print(f"Casa: {cont} - grãos: {grãos}")
   soma += grãos

print("Total de grãos no tabuleiro:", soma)

#Fim.