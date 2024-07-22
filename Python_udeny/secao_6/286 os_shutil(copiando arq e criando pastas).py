# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35348702#questions
# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil
# caminho = os.path.join('e:\\music', 'genero', 'comedia')

HOME = os.path.expanduser('~')  # Caminho do usuário no windows
print(HOME)
DESKTOP = os.path.join(HOME, 'onedrive\\desktop')  # destino da cópia
print(DESKTOP)
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Duo')  # pasta a ser copiada
# para dentro da outra (NOVA_PASTA)
print(PASTA_ORIGINAL)
NOVA_PASTA = os.path.join(DESKTOP, 'Cria_do_python')  # pasta a ser criada

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminnho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminnho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminnho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminnho_novo_arquivo)
