#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34599200#questions/19560002
#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34599454#questions/19560002
#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34599542#questions/19560002
#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34600162#questions/19560002
for i in range(0,10,2): # passa de zero a dez pulando de 2 em dois
    print(f'{i}',end=' ')
print('\n---------------------------')#apenas para pular uma linha

lista = ['Edson','Laine','Bianca','Luisa']
for nome in lista: 
    print(nome) #pega cado nome da lista.
print('\n---------------------------')#apenas para pular uma linha

for i, nome in enumerate(lista): 
    print(f'{i}', end=' ') #pega cada indice da lista.
    print(f'{nome}', end=' ') #pega cada nome da lista.
print('\n---------------------------')#apenas para pular uma linha

for item in enumerate(lista):
    print(f'{item}', end=' ') #pega cada nome junto com o índice.
    indice, nome = item #pega separado (indice e nome), em cada variável
    print(indice, nome)    
print('\n---------------------------')#apenas para pular uma linha

for i in range(len(lista)): #isso faz o mesmo efeito do for acima.
    print(f'{i}', end=' ')
print('\n---------------------------')#apenas para pular uma linha

lista_enumerada = list(enumerate(lista, start=3)) #converte a lista em um list com (indice, valor). O start(facultativo) é onde começa o indice.
print(lista_enumerada)


print('\n---------------------------')#apenas para pular uma linha
grupos =[
    ['maria','helena'],
    ['elaine'],
    ['luiz','joão','eduarda','edson']
]
for sala in grupos:
    print(f'A sala é composta por {sala}')
    for aluno in sala:
        print(aluno)