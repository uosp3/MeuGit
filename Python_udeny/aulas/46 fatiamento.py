# fatiamento [i:f:p] - (i)nicio, (f)im, (p)asso
# início e fim podem ser omititos, se for o caso. [::]
variavel = 'Olá, Mundo!'
print(variavel[5:])#pega parte da variável a partir da posição 5 até o final.
print(variavel[:4])#pega parte da variável do ínico (zero) até a posição 3. Veja que o valor usado foi 4 mas so pega até a posição anterior.
print(variavel[0:11:2])#pega do ínicio até o fim, de 2 em 2 caracteres
print(variavel[::2])#faz o mesmo que a linha acima, ínicio e fim foram omitidos e isto indica que deve ser considerado tudo.
print(variavel[::-2])#faz o mesmo que a linha acima, ínicio e fim foram omitidos e isto indica que deve ser considerado tudo e agora foi de traz pra frente.