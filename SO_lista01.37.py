#Algoritmo Lt01.37.

#Declarar.
num : int = 0
aux1 : int = 0
aux2 : int = 0
soma : int = 1

#Inicio.
num = int(input("Insira um número: "))
print(f"\nSérie de Fibonacci: {soma}", end="  ")

for cont in range (1, num, 1):
   aux1 = soma
   soma = aux1 + aux2
   aux2 = aux1
   print(soma, end="  ")

#Fim