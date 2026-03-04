#Algoritmo SO_Lista01.15
#Declarar.
c1: float = 0;
c2: float = 0;
hip: float = 0;
#Início.
c1 = float(input("Cateto 1:"));
c2 = float(input("Cateto 2:"));
hip = (c1**2 + c2**2)**0.5;
print("Hipotenusa:", hip);
#FIM.