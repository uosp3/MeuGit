#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34692812#questions/19560002
# exemplo de como deixar apenas uma letra, no caso a última, como maiúscula.
nomes=['luiz', 'edson', 'laine', 'luisa', 'bianca']
novo_nomes=[f'{nome[:-1].lower()}{nome[-1].upper()}'
             for nome in nomes
             ] 
print(novo_nomes)


lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)