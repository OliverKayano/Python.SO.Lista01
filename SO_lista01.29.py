#Algoritmo Lt01.29

#Declarar.
invest : int = 0
valor : float = 0.0

#Inicio.
print("1 - Poupança (3% ao mês)")
print("2 - Renda fixa (5% ao mês)")

invest = int(input("Insira o número do investimento: "))
valor = float(input("Valor do investimento: "))

if invest == 1 and valor >= 0:
   valor = valor*1.03
   print(f"Valor corrigido (poupança): {valor:.2f}")

elif invest == 2 and valor >= 0:
   valor = valor*1.05
   print(f"Valor corrigido (renda fixa): {valor:.2f}")

else:
   print("Tipo de investimento ou valor inválido.")

#Fim.