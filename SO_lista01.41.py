#Algoritmo Lt01.41.

#Declarar.
dado1 : int = 0
dado2 : int = 0
soma : int = 0

#Inicio.
print ("Combinação de dados cuja soma será 7:")

for dado1 in range(1, 7, 1):

   for dado2 in range(1, 7, 1):
      soma = dado1 + dado2

      if soma == 7:
         print(dado1, "e", dado2)

#Fim.