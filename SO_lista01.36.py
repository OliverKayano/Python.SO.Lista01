#Algoritmo Lt01.36.

#Declarar.
num : int = 0
fatorial : int = 1
soma : float = 1.0

#Inicio.
num = int(input("Insira um valor: "))
print (f"\nSérie: {soma}", end="")

for aux in range (1, (num+1), 1):
   fatorial = fatorial*aux
   soma += 1/fatorial
   print(f" + 1/{fatorial}", end="")

print(f"\n\nSoma = {soma}")

#Fim.