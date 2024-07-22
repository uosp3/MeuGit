#tuplas pode ter elementos de vários tipos (int, str, etc...)
lanche= ("Hamburger","Suco","Pizza","Pudim","Batata Frita")
print(lanche)
print(sorted(lanche))#mosta em ordem alfa

a = (2,5,4)
b = (5,8,1,2)
c = b + a
d = a + b # é diferente de b + a, so concatena.
print(c)
print(d)
print(c.count(5))#conta os elementos 5
print(c.index(8))#mostra a posição do elemento 8
print(c.index(5,1))#mostra a posição do elemento, a partir da posição 1. Serve para o caso de existir dois elementos iguais na tupla.
del(d)#deleta a tupla.