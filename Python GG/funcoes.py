def funcao(* p): #nesse caso não se sabem quantos parâmetros serão passados.
    pass
#-----------------------------------------------------------------------------
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1
valores=[6,3,9,1,0,2]
dobra(valores)
print(valores)
#-----------------------------------------------------------------------------
def soma(* numeros):
    s=0
    for num in numeros:
        s += num
    print(f'Somando os valores {numeros} temos {s}')

soma(5,2,4,3,13)
#-----------------------------------------------------------------------------
#DOCSTRING é um help que pode ser colocado em funcões (nos comentários) para que outras pessoas saibam o que exatamente a função faz.
#-----------------------------------------------------------------------------
#PARÂMETROS OPCIONAIS - são valores atribuidos aos parâmetros das funções de forma que se não forem passados serão considerados os valores previamente atribuidos.
#Exemplo
def somar(a=0, b=0, c=0):
    pass
#a chamada da função pode ser com um, dois ou tres parâmetros. O que não for informado será considerado zero.
#-----------------------------------------------------------------------------
#ESCOPO DE VARIÁVEIS
def teste(b):
    b+=4
    c=2

a=5
teste(a)

#Neste caso, 'a' vale dentro e fora da função, mas 'b' e 'c' so valem dentro da função
#ATENÇÃO: Se for criada uma nova variável 'a' dentro da função o programa terá duas variáveis 'a' distintas.
#OBS.: Se 'a' for definida como global, dentro da função, a variável 'a' será a mesma dentro e fora da função.
#-----------------------------------------------------------------------------
#RETORNO DE VALORES (return)
def somar(a=0, b=0, c=0):
    s=a+b+c
    return s #devolve para a chamada da função o resultado da função.

r1=somar(3,2,5)
r2=somar(1,7)
r3=somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')

