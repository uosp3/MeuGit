# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34784946#questions/19560002
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34785430#questions/19560002
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34785464#questions/19560002
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34785922#questions/19560002
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
import os
caminho_arquivo = 'E:\\Cursos\\Tudo\\Python_udemy\\aula116.txt'
# OBS.....no windows o caminho do arquivo deve ser colocado com duas \\(barras)
# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')

with open(caminho_arquivo, 'w+', encoding='UTF-8') as arquivo: #Atenção, 'w' apaga o que tiver no arquivo. Nesse caso melhor usar o 'a'
    arquivo.write('Atenção..\n')#para mostrar caracteres acentuado clicar em utf8 na barra de status o vscode e mudar a codificação para windows 1252
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())


print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

#leitura recomendada
#https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

#input()# a linha abaixo apaga o arquivo, este input é apenas para gerar uma pausa no código para que se veja o arquivo antes da exclusão.
#os.remove(caminho_arquivo) #ou os.unlink()

os.rename(caminho_arquivo, 'aula116-2.txt') #renomear o arquivo
