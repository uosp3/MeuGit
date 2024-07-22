import os


def check_chromedriver():
    chromedriver_path = 'C:\\Users\\uosp3_\\AppData\\Local\\SeleniumBasic'
    # Substitua com seu caminho absoluto

    if os.path.exists(chromedriver_path):
        print(f'ChromeDriver encontrado em: {chromedriver_path}')

        # Verificar a versão do ChromeDriver (alternativa)
        try:
            size = os.path.getsize(chromedriver_path)
            print(f'Tamanho do ChromeDriver: {size} bytes')
        except Exception as e:
            print(f'Erro ao obter informações do ChromeDriver: {e}')
    else:
        print(f'ChromeDriver não encontrado no caminho: {chromedriver_path}')


if __name__ == '__main__':
    check_chromedriver()
