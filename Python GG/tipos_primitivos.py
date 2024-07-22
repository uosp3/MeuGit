algo=0
while algo !="":
    algo=input("Digite algo: ".format(e))
    print("O tipo primitivo desse dado é ", type(algo))
    print("Só tem espaços?.............. ", algo.isspace())
    print("É um número? ................ ", algo.isnumeric())
    print("É alfabético? ............... ", algo.isalpha())
    print("É alfanumérico? ............. ", algo.isalnum())
    print("Está em maiúsculo? .......... ", algo.isupper())
    print("Está em minúsculo? .......... ", algo.islower())
    print("Está capitalizada? .......... ", algo.istitle())# começa com maiúscula

