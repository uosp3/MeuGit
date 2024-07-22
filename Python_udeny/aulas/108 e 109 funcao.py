#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34639820#questions
def soma(x, y, z):
    print(x+y)

soma(1,y=2, z=4)#se um parâmetro for nomeado, todos os outros que estiveem apóes ele deverão ser nomeados
print('..'*20)

#Escopo (global e local)
#call stack - pilha de chamadas.
#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34639828#questions
x=3 #outro x foi definido dentro da função, e não tem relação com este
print(f'{x=}')
def escopo():
    global x
    x=4 #valor definido dentro da função não pode ser usado fora da função
    y=5
    def outra_funcao():
        y=2#esse y dentro dessa função so é acessível nessa função
        print(f'{x=},{ y=}')
    outra_funcao()
    print(f'{x=}')
    print(f'{y=}')#esse y é o de valor 10, definido fora da função antes da chamada

y=10 # valor definido antes da chamada da função pode ser usado na função
print(f'{y=}')
escopo()
print(f'x global {x=}')

#*args para quantidade de argumentos não nomeados
def soma2(*args):
    print(args, type(args))

soma2(1,2,3,4,5,6)
