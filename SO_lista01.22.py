#Algoritmo_Lt01.22.

#Declarar.
num1 : int = 0
num2 : int = 0

#Inicio.

num1, num2 = map(int, input("Insira 2 números inteiros (separados por espaço): ").split())

if num1 > num2:
   print ("Ordem crescente: ", num1, ",", num2)

else:
   print ("Ordem crescente: ", num2, ",", num1)

#Fim.