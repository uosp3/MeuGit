import re
import os

nome="aula46_teste.txt"
caminho="E:/Cursos/Tudo/Python/"
if os.path.exists(caminho+nome):
    print("Arquivo ja existe")
else:
    f=open(caminho+nome,"x") #caminho do arquivo a ser aberto
    print("O arquivo foi criado.")
    f.close()   

deletar=input("Deseja deletar o arquivo? (s/n)")

if deletar=="s":
    os.remove(caminho+nome)