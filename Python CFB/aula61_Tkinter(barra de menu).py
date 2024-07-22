#https://www.youtube.com/watch?v=MK6e3Tj8dS4&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=61
from tkinter import *
import os

def semComando():
    print()

app=Tk()
app.title("CFB Cursos")#titulo da janela
app.geometry("500x300")#tamanho da janela
app.configure(background="#dde")#cor de fundo

barraDeMenus=Menu(app)#cria o menu
menuContatos=Menu(barraDeMenus,tearoff=0)#cria um menu dentro da barra de menus. O 'tearoff=0' tira um pontilhado(tipo um separador) que aparece no menu
menuContatos.add_command(label="Novo",command=semComando)#adiciona um comando ao menuContatos
menuContatos.add_command(label="Pesquisar",command=semComando)
menuContatos.add_command(label="Deletar",command=semComando)
menuContatos.add_separator()#cria uma separação no menu
menuContatos.add_command(label="Fechar",command=app.quit)
barraDeMenus.add_cascade(label="Contatos",menu=menuContatos)#definir o menu e os itens(menuContatos) dele

menuManutencao=Menu(barraDeMenus,tearoff=0)
menuManutencao.add_command(label="Banco de Dados",command=semComando)
barraDeMenus.add_cascade(label="Manutenção",menu=menuManutencao)

menuSobre=Menu(barraDeMenus,tearoff=0)
menuSobre.add_command(label="CFB Cursos",command=semComando)
barraDeMenus.add_cascade(label="Sobre",menu=menuSobre)



app.config(menu=barraDeMenus)
app.mainloop()#gera uma janela