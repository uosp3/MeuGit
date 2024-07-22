n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))
resto_da_divisão= n1%n2
divisao_inteira= n1//n2
potencia=n1**n2
potencia2=pow(n1,n2)
soma=n1+n2
multiplicacao=n1*n2
divisao=n1/n2

print("A soma é {}, o produto é {} e a divisão é {:.3f}".format(soma, multiplicacao, divisao), end=" # ") # o .3f faz a divisão ficar com 3 casas decimais(float). O "end=' # '" faz com que a o próximo print fique nesta mesma linha
print(" a divisão inteira é {} e a potência é {}".format(divisao_inteira,potencia))


print("Edson = "*10)#olha isso...repete 10 vezes o que está escrito
