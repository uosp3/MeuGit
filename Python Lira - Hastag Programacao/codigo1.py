#começar com passo a passo do projeto, em portugues.
#1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE=.7 #pausa a cada comando

#pyautogui.python - consultar documentação
#abrir o nagegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#dar uma pausa um pouco maior(3 segundos)
time.sleep(3) #import time

pyautogui.click(x=1547, y=436)
#2: Fazer login
pyautogui.write("meu@email.com.br")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("tab")

#3: Importar base de dados
import pandas#pip install pandas numpy openpyxl
tabela=pandas.read_csv("produtos.csv")#importa a base de dados

#4: cadastrar 1 produto
#para cada linha
for linha in tabela.index:#index para linha, colunns para colunas
    pyautogui.click(x=1528, y=313)

    codigo=tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab") 

    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    obs=tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(5000)#positivo pra cima, negativo pra baixo.

#5: Repetir o processo até acabar
#15719 sorteio