#https://www.youtube.com/watch?v=a7DH88vk2Sk&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=31
#FATIAMENTO
frase="Curso em Vídeo Python"
print(frase[9])#pega a 10ª letra do texto 
print(frase[9:13])#pega parte do texto, começando em 9 e até 12, o 13 não aparece no resultado.
print(frase[9:21:2])#pega parte do texto, começando em 9 e até 21, pulando de 2 em 2.
print(frase[:5])#pega parte do texto, começando em 0 e até 4, o 5 não aparece no resultado. Neste caso começou em zero porque o início foi omitido, seria o mesmo que 'frase[0:5]
print(frase[15:])#pega parte do texto, começando em 15 e até o fim
print(frase[9::3])#pega parte do texto, começando em 9 e até o fim(o fim foi omitido), pulando de 3 em 3

#ANALISE
print(len(frase))#comprimento do texto
print(frase.count("o"))#conta quantas letras 'o' tem no texto
print(frase.count("o",0,14))#conta quantas letras 'o' tem no texto começando em zero indo até 13, o 14 não conta.
print(frase.find("deo"))# pega a posição INICIAL, no texto, em que aparece 'deo', se 'deo' não for encontrado retorna -1
print(frase.rfind("deo"))# pega a posição FINAL, no texto, em que aparece 'deo', se 'deo' não for encontrado retorna -1
print("Curso" in frase) # se 'Curso' for encontrado no texto retorna 'True'

#TRANSFORMAÇÃO
print(frase.replace("Python","Android"))#substitui uma palavra pela outra no texto.
print(frase.upper())#passa o texto todo para maiúsculo
print(frase.lower())#passa o texto todo para minúsculo
print(frase.capitalize())#passa a primeira letras para miúscula e o resto fica minúsculo
print(frase.title())#passa a primeira letra (de cada parte do texto) para maiúsculo

frase="   Aprenda Python  "# com espaços antes de depois
print(frase)
print(frase.strip())#remove espaços antes e depois do texto.
print(frase.rstrip())#remove espaços antes do texto.
print(frase.lstrip())#remove espaços depois do texto.

#DIVISÃO
frase="Curso em Vídeo Python"
print(frase.split())#divide o texto em pedaços separados por espaço, criando uma lista.

#JUNÇÃO
print("-".join(frase))#divide o texto, letra por letra, separando por '-'

#OBS.: Para imprimir texto longo use tres aspas antes e tres aspas depois do texto.