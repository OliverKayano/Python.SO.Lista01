#Algoritmo SO_Lista01.05
#Declarar.
A: float = 0;
B: float = 0;
C: float = 0;
raiz1: float = 0;
raiz2: float = 0;
#Iniciar.
A = float(input("Valor de A:"));
B = float(input("Valor de B:"));
C = float(input("Valor de C:"));
raiz1 = ((-B + (((B*B)-(4*A*C))**0.5))/(2*A));
raiz2 = ((-B - (((B*B)-(4*A*C))**0.5))/(2*A));
print("Raíz 1:", raiz1);
print("Raíz 2:", raiz2);
#FIM.