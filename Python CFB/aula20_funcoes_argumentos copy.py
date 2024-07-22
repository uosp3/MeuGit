def somar(n1,n2):
    r=n1+n2
    print("Soma de ",n1,"e",n2,"=",r)

somar(5,7)
somar(12,8)
somar(1,2)

def textos(*txt):#com o * pode se passar quantos parâmetros forem necessários, arbitrário
    for t in txt:        
        print(t)

textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")

def somar2(*num):
    r2=0
    for n in num:        
        r2+=n
    print("\nSoma = ",r2)

somar2(5,2,4,8,9,13)

valores=[1,5,3,2]
def somar3(num):#nesse caso foi passada uma lista como argumento que é considerado com um único argumento.
    r=0
    for n in num:
        r+=n
    print("\nSoma = ",r)
somar3(valores)


def carros(c="Civic"):#se o argumento for passado ele será considerado, caso contrário será considerado o argumento "Civic"
    print("\nModelo: ",c)

carros("Focus")