#Algoritmo Lt01.28.

#Declarar.
preço : float = 0.0
média: float = 0.0

#Inicio.
preço, média = map(float, input("Preço atual e média mensal (separados por vírgula)").split(","))

if preço < 30 and média < 500:
   preço = preço*1.1

elif 30 <= preço and preço < 80 and 500 <= média and 1000 > média:
   preço = preço*1.15

elif preço >= 80 and média >= 1000:
   preço = preço*0.95

print(f"Novo preço: {preço:.2f}")

#Fim.