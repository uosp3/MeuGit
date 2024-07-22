#passo a passo do projeto
# 1 - abrir sistema da empresa
        # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # pip install pyautogui
import pyautogui
from time import sleep

pyautogui.PAUSE = .7
    # abrir o navegadortipo 
pyautogui.press('win')
pyautogui.write('chome')
pyautogui.hotkey('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.hotkey('enter')
sleep(3)
pyautogui.click(x=1628, y=524)
# 2 - fazer login
pyautogui.write('uosp3gs@gmail.com')
pyautogui.hotkey('tab')
pyautogui.write('senha')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
    # entrar no site do sistema
# 3 - abrir/importar base de dadas de produtos para cadastrar
# pip install pandas numpy openpyxl
import pandas as pd
tabela = pd.read_csv('produtos.csv')

#print(tabela)

# 4 - cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=1619, y=408)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.hotkey('tab')

    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.hotkey('tab')

    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.hotkey('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.hotkey('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario']).replace('.',',')
    pyautogui.write(preco_unitario)
    pyautogui.hotkey('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.hotkey('tab') 

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    pyautogui.hotkey('home')
    #pyautogui.scroll(5000)


# 5 - repetir isso tudo até acabar a lista de produtos
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

