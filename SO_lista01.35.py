#Algoritmo Lt01.35.

#Declarar.
num1 : int = 0
num2 : int = 0
soma : int = 0

#Inicio.
num1, num2 = map(int, input("Insira 2 números inteiros, separados por vírgula: ").split(","))

if num1 <= num2:
   soma = num2
   num2 = num1
   num1 = soma
   soma = 0

if num2 % 2 == 0:
   num2 += 1

for (num2) in range (num2, num1, 2):
   soma += num2

print("Soma dos números ímpares do intervalo:\nSoma =",soma)

#Fim.