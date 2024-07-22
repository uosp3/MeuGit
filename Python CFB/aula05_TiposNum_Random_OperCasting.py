#https://www.youtube.com/watch?v=Vsrhr5bh5u0&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=5

import random #necessário para usar esta função no código

num_i=10
num_f=5.2
num_c=1j #numeros complexos

num_r=random.randrange(0,59) #gera um número aleatório entre 0 e 59.

x=num_r

print("Valor: " + str(x) + " - Tipo: " +str(type(x))) #str converte os dados para string para concatenar.

num_r=[#gera um array/list com 6 números aleatórios
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59)
]

x=num_r

print("Valor: " + str(x) + " - Tipo: " +str(type(x))) #str converte os dados para string para concatenar.