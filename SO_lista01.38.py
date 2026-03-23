#Algoritmo Lt01.38.

#Declarar.
maior : int = 0
menor : int = 0
entrada : int = -9

#Inicio.

for cont in range(1, 101):
   entrada = int(input(f"Insira o {cont}o termo: "))
   
   while entrada < 0:
      entrada = int(input(f"Insira o {cont}o termo: "))

   if cont == 1:
      maior = entrada
      menor = entrada

   elif entrada > maior:
      maior = entrada

   elif entrada < menor:
      menor = entrada

print(f"\nMaior valor: {maior}\nMenor valor: {menor}")

#Fim.