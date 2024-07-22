#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34692166#questions/19560002
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)
print('_'*30)
#as linhas acima podem ser feitas conforme linhas abaixo
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)
print('_'*30)
##########################################################
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)