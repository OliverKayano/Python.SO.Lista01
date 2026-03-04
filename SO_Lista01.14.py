#Algoritmo SO_Lista01.14
#Declarar.
ang1: float = 0;
ang2: float = 0;
ang3: float = 0;
#Início.
ang1 = float(input("Valor do primeiro ângulo:"));
ang2 = float(input("Valor do segundo ângulo:"));
ang3 = 180 - ang1 - ang2;
print("Terceiro ângulo:", ang3);
#FIM.