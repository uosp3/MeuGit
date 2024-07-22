import os
import subprocess


def convert_ui_to_py(ui_file):
    # Define o nome do arquivo .py correspondente
    py_file = os.path.splitext(ui_file)[0] + '.py'
    # Comando para converter o arquivo .ui para .py
    command = ['pyuic5', '-x', ui_file, '-o', py_file]
    # Executa o comando
    subprocess.run(command, check=True)
    # Informa que o arquivo foi convertido
    print(f'Converted {ui_file} to {py_file}')


def convert_all_ui_files(directory):
    # Itera sobre todos os arquivos no diretório especificado
    for ui_file in os.listdir(directory):
        # Verifica se o arquivo termina com .ui
        if ui_file.endswith('.ui'):
            # Converte o arquivo .ui para .py
            convert_ui_to_py(os.path.join(directory, ui_file))


if __name__ == '__main__':
    # Define o diretório como o diretório atual
    directory = os.path.dirname(os.path.realpath(__file__))
    # Converte todos os arquivos .ui no diretório atual
    convert_all_ui_files(directory)
