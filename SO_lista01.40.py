#Algoritmo Lt01.40.

#Declarar.
num1 : int = 0
num2 : int = 0
aux1 : int = 0
aux2 : int = 0

#Iniciar.
num1, num2 = map(int, input("Insira 2 números inteiros, separados por espaço: ").split())
print("\nNúmeros primos no intervalo:")

if (num2 > num1):
   aux1 = num2
   num2 = num1
   num1 = aux1

for cont in range(num2, (num1 +1), 1):
   aux2 = 2

   while (aux2 < cont) and (cont % aux2 != 0):
      aux2 += 1

   if (aux2 == cont):
      print (cont)

#Fim.