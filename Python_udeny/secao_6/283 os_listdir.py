# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35321388#questions
# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os
# E:\Cursos\Tudo\Python_udemy
caminho = os.path.join('e:\\cursos', 'tudo', 'python_udemy')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print('Pasta :', pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
