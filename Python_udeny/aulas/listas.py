lista = ['edson', 'gomes', 123, True]
print(lista[1][3])
lista.insert(2, "inserido") #insere um valor no índice 2

lista.append('teste') #acrescenta um valor à lista
print(lista)

ultimo=lista.pop()
lista.append('teste')
lista.pop()#deleta o último elemento da lista
print(lista, 'Removi o ', ultimo)

lista.append('teste')
lista.pop(3) # remove o elemento de índice 1
print(lista)

del lista[-1] #deleta o último elemento

lista.clear() #limpa a lista
print(lista)

lista_a=[1,2,3]
lista_b=[4,5,6]
lista_d=lista_a.copy() #neste caso os valores de 'a' foram copiados para 'd' e a alteração abaixo, feita em 'a' não afeta 'd'
lista_a[2]=10 
lista_e=lista_a #neste caso as alterações feitas em 'a' afetam 'e'
print(f'{lista_e=}')
lista_c=lista_a+lista_b # junta duas listas em uma terceira

lista_a.extend(lista_b) # altera a lista 'a', colocando o valores de 'b'
print(f'{lista_c=}')
print(f'{lista_a=}')
print(f'{lista_d=}')

#listas dentro de listas
grupos =[
    ['maria','helena'],
    ['elaine'],
    ['luiz','joão','eduarda',(0,10, 20, 30, 40)]
]
print(grupos)
print(grupos[2])
print(grupos[2][1])
print(grupos[0][1])
print(grupos[2][3][2])
