lanche= ["Hamburger","Suco","Pizza","Pudim","Batata Frita"]
print(lanche)
lanche[3]="Misto" #substitui o item de indice 3
print(lanche)
lanche.append("Doce")#adiciona um elemento no final da lista
print(lanche)
lanche.insert(2,"Pao")#adiciona um elemento na posição indicada.
print(lanche)
lanche.sort()#coloca em ordem alfa
print(lanche)
lanche.sort(reverse=True)#coloca em ordem alfa decrescente.
print(lanche)
del lanche[3]#deleta o elemento da posição indecada
print(lanche)
lanche.pop(3)#faz o mesmo que alinha 13
print(lanche)
lanche.pop()#deleta o último elemento. A posição não é indicada.
print(lanche)
lanche.remove("Suco")#deleta o elemento pelo valor(nome), se existirem dois iguais apenas o primeiro da lista será deletado.
print(lanche)
valores=list(range(4,11))#cria uma lista de 4 até 10. O último não entra
print(valores)
valores=list(range(4,11,2))#faz o mesmo que a linha 21 de 2 em 2
print(valores)
print(len(valores))#mostra a quantidade de elementos
teste=[]#cria uma lista vazia.
teste2=list()#tb cria uma lista vazia.

for c, v in enumerate(valores):#pega o índice(chave) e o valor
    print(f"Na posição {c} encontrei o valor {v}!")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a=[2,3,4,7]
c=a #aqui foi feita uma ligação de "c" com "a"
#no códibo abaixo ao alterar o valor de c[2] o mesmo vai acontecer em 'a', mesmo que a alteração seja depois que o "a" e "c" foram definidos.
c[2]=9
#fazendo uma cópia, ou seja b=a[:] a alteração so acontecerá em "b"
b=a[:]#aqui foi feita uma cópia de "a" para "b"
b[2]=8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
print(f"Lista B: {c}")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



pessoas=[["Pedro", 25],["Maria", 19],["João", 32]]
print(pessoas[0][0]) #Pedro
print(pessoas[1][1]) #19
print(pessoas[2][0]) #João
print(pessoas[1])    #["Maria", 19] 
for p in pessoas:
    print(f"{p[0]} tem {p[1]} anos de idade")
