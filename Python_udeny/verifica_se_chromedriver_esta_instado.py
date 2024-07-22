import os
import subprocess


def check_chromedriver():
    # Especifique o caminho absoluto para o chromedriver aqui
    chromedriver_path = 'C:\\Users\\uosp3_\\AppData\\Local\\SeleniumBasic'
    # Substitua com seu caminho absoluto

    if os.path.exists(chromedriver_path):
        print(f'ChromeDriver encontrado em: {chromedriver_path}')

        # Verificar a versão do ChromeDriver
        try:
            result = subprocess.run([chromedriver_path, '--version'],
                                    capture_output=True, text=True)
            version_output = result.stdout.strip()
            print(f'Versão do ChromeDriver: {version_output}')
        except Exception as e:
            print(f'Erro ao obter a versão do ChromeDriver: {e}')
    else:
        print(f'ChromeDriver não encontrado no caminho: {chromedriver_path}')


if __name__ == '__main__':
    check_chromedriver()
