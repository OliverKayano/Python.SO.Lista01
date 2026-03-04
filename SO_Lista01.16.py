#Algoritmo SO_Lista01.16
#Declarar.
h: float = 0;
vh: float = 0;
desc: float = 0;
dep: int = 0;
sb: float = 0;
sl: float = 0;
#Início.
h = float(input("Horas trabalhadas: "));
vh = float(input("Valor hora: "));
desc = float(input("Desconto em porcentagem: "));
dep = int(input("Número de dependentes: "));
sb = h*vh;
sl = sb - (sb*desc/100) + (100*dep);
print("Salário líquido:", sl);
#FIM.