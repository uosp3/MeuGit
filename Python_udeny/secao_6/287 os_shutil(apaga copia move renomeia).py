# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35349000#questions
# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~')
ORIGEM = os.path.join(HOME, 'OneDrive\\Desktop')
DESTINO = 'E:\\Cursos\\Tudo\\Python_udemy\\Teste'
PASTA_COPIADA = os.path.join(ORIGEM, 'Duo')
PASTA_CRIADA = os.path.join(DESTINO, 'Criada_pelo_python')

shutil.rmtree(PASTA_CRIADA, ignore_errors=True)  # apaga a pasta, se existir
# se ela existir

shutil.copytree(PASTA_COPIADA, PASTA_CRIADA)  # copia os arquivos
# shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')
# shutil.rmtree(NOVA_PASTA, ignore_errors=True)

# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminnho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         os.makedirs(caminnho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminnho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_arquivo, caminnho_novo_arquivo)
