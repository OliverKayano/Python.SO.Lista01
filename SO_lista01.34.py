#Algoritmo Lt01.34

#Declarar.
cont : int = 1
num : int = 0
tabuada : int = 1

#Inicio.
num = int(input("Insira um número: "))
print(f"Tabuada do {num}:")

for cont in range (cont, 11, 1):
   tabuada = num*cont
   print(f"{num}x{cont} = {tabuada}")

#Fim.