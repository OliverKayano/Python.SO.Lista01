#Algoritmo Lt01.20.

#Declarar.
A: float = 0.0
B: float = 0.0
C: float = 0.0
raiz1: float = 0.0
raiz2: float = 0.0
delta: float = 0.0

#Inicio.

A = float(input("Insira o valor de A: "))
B = float(input("Insira o valor de B: "))
C = float(input("Insira o valor de C: "))
delta = B*B - 4*A*C

if delta >= 0:
   raiz1 = (-B + delta**0.5) / (2*A)
   raiz2 = (-B - delta**0.5) / (2*A)
   print("Raízes reais: \n", raiz1, ",", raiz2)
   
else:
   print("Raízes imaginárias.")

#Fim.