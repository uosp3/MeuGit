#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34623838#questions/19560002
frase = 'olha so que, coisa interessante'
lista_frases = frase.split(',') #divide a frase usando a vírgula como separador
print(lista_frases)
lista_frases = frase.split(' ') #divide a frase usando o espaço como separador
print(lista_frases)
juntando_frase=' '.join(lista_frases)#junta as partes usando espaço entre elas
print(f'{juntando_frase=}')

frase = '  olha so que, coisa interessante  '
print(frase)
print(frase.strip())#tira espaços antes e depois do texto (lstrip tira so da esquerda, rstrip tira so da direita)