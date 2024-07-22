#\033[0;33;44m - stylo, text, background
#\033[m - volta ao padrão
#style(0 - sem estilo, 1 - negrito, 4 - sublinhado, 7 - negative(inverte as cores) )
#text(30 - branco, 31 - vermelho, 32 - verde, 33 - amarelo , 34 - azul, 35 - magenta, 36 - ciano, 37 - cinza)
#background(40 - branco, 41 - vermelho, 42 - verde, 43 - amarelo , 44 - azul, 45 - magenta, 46 - ciano, 47 - cinza)

print("\033[1;31;43m Olá, Mundo!\033[m")
print("\033[4;30;45m Olá, Mundo!\033[m")
print("\033[7;30;45m Olá, Mundo!\033[m")#7(negativo) inverte as cores

print("Colorir uma \033[33m parte\033[m do texto em uma frase")

nome="Edson"
cores={'verde':'\033[4;32m','limpa':'\033[m'}#pode acrescentar várias cores
print("Ola! Muito prazer em te conhecer, {}{}{}!!!".format(cores['verde'], nome,cores["limpa"]))