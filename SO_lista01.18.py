#Algoritmo SO_lista01.18.
#Declarar.
v1 : int = 0; 
v2 : int = 0; 
d : int = 0;
#Inicio.
v1 = int(input("Insira o primeiro valor: "));
v2 = int(input("Insira o segundo valor: "));
if (v1>v2):
    d = (v1-v2);
    print ("diferenca: ", d);
elif (v2>v1):
    d = (v2-v1);
    print ("diferenca: ", d);
else:
    print ("diferenca: ", 0);
#Fim.

