numeros = [[numero, numero ** 2] for numero in range(10)]
print(numeros)
flat = [y for x in numeros for y in x]
print(flat)

#explicação: no flat teria: x for x in numeros
#pega isso (x for x in numeros) e coloca dentro de outro for, ou seja,
# 'isso' for y in x, que no final é colocado em 'y'.
# vide https://www.youtube.com/watch?v=1YbTDczvqco a partir do instante 35