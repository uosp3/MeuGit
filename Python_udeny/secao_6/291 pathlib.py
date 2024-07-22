# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35431058#questions/21564524
# https://www.youtube.com/watch?v=T17BTNKBeJY
from pathlib import Path

caminho_projeto = Path()
print('*'*30)
print(caminho_projeto.absolute())  # absolute para pegar o caminho completo
print('*'*30)
caminho_arquivo = Path(__file__)  # pega o caminho(todo) até o nom do  arquivo
print(caminho_arquivo)
print(caminho_arquivo.parent)  # pega o caminho(todo) sem o nome do arquivo
print(caminho_arquivo.parent.parent)  # pega o caminho, até a pasta anterior

print(Path.home() / 'Desktop')  # pega a pasta do usuário, no SO, + desktop
# apenas gera o caminho na memória, não cria a pasta em arquivo.

arquivo = Path.home()/'OneDrive'/'Desktop'/'arquivo.txt'
arquivo.touch()  # Gera/cria o arquivo no caminho acima
arquivo.write_text('Ola, mundo!')  # escreve no arquivo
print(arquivo.read_text())  # lê o arquivo

arquivo.write_text('')  # apaga o conteudo do arquivo

with arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('outra linha\n')

print(arquivo.read_text())

arquivo.unlink()  # apaga o arquivo

cria_pasta = Path.home()/'OneDrive'/'Desktop' / 'Criada_com_pathlib'
cria_pasta.mkdir(exist_ok=True)  # cria uma pasta, True para ignorar se exisitr

sub_pasta = cria_pasta / 'sub_pasta'
sub_pasta.mkdir(exist_ok=True)  # cria outra pasta dentro da criada acima

outro_arquivo = sub_pasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Beleza')


files = sub_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file1 = files / f'file_{i}.txt'

    if file1.exists():
        file1.unlink()
    else:
        file1.touch()

    with file1.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree(sub_pasta)
