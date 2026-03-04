#Algoritmo SO_Lista01.12
#Declarar.
n: int = 0;
ano: int = 0;
idade: int = 0;
idade17: int = 0;
#Início.
n = float(input("Inserir ano de nascimento:"));
ano = float(input("Insetir ano atual:"));
idade = (ano-n);
idade17 = idade + 17;
print("Idade atual:", idade);
print("Idade daqui 17 anos:", idade17);
#FIM.