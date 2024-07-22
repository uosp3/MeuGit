"""
Automatizar minhas msg para clientes. Quero mandar msg de cobrança em determinado dia com clientes com vencimento diferente
"""
#https://www.youtube.com/watch?v=gv9dRvkn0rI
import openpyxl
from urllib.parse import quote #para formatar a msg
import webbrowser
from time import sleep
import pyautogui

webbrowser.open("https://web.whatsapp.com/")
sleep(60)
#ler planilha e guarda informações
workbook = openpyxl.load_workbook("clientes.xlsx")
pagina_clientes = workbook['Plan1']

for linha in pagina_clientes.iter_rows(min_row=2):#começa os dados da linha 2
    nome = linha[0].value #primeira coluna no excel
    telefone = linha[1].value #primeira coluna no excel
    vencimento = linha[2].value #primeira coluna no excel
    
    mensagem = f'Olá {nome} seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Favor pagar no link https://www.link_do_pagamento.com'

    #criar links personalizados do zap e enviar msg para cada cliene
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        #https://web.whatsapp.com/send?phone=5533999233433&text="o texto a enviar"
        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
        seta=pyautogui.locateAllOnScreen("seta.png")
        sleep(5)
        pyautogui.click(seta[0],seta[1])
        sleep(5)
        pyautogui.press("ctrl",'w')
        sleep(5)
    except:
        print(f'Não foi possível enviar mensagem para {nome}')
        with open("erros.csv","a", newline='', encoding="utf-8" ) as arquivo:
            arquivo.write(f'{nome}, {telefone}')


#ver com esta bib pywhatkit 