#https://www.youtube.com/watch?v=kXj4CDBJyYY&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=60
from tkinter import *
import os
import aula53a56_agenda.banco as banco

def gravarDados():
    if tb_nome.get() != "":
        vnome=tb_nome.get()
        vfone=tb_fone.get()
        vemail=tb_email.get()
        vobs=tb_obs.get("1.0",END)
        vquery="insert into tb_contatos (t_nomecontato, t_telefonecontato, t_emailcontato, t_obs) values('"+vnome+"','"+vfone+"','"+vemail+"','"+vobs+"')"
        banco.dml(vquery)
        tb_nome.delete(0,END)
        tb_fone.delete(0,END)
        tb_email.delete(0,END)
        tb_obs.delete("1.0",END)
        print("Dados gravados")
    else:
        print("Erro")


app=Tk()
app.title("CFB Cursos")#titulo da janela
app.geometry("500x300")#tamanho da janela
app.configure(background="#dde")#cor de fundo

Label(app,text="Nome",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)#cria um label dentro do app, cor de fundo cor da letra e ponto cardeal  
#place faz o label aparecer, onde aparecer e de que tamanho.
tb_nome=Entry(app)#caixa de texto de uma linha
tb_nome.place(x=10,y=30,width=200,height=20)

Label(app,text="Telefone",background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=100,height=20)
tb_fone=Entry(app)
tb_fone.place(x=10,y=80,width=100,height=20)

Label(app,text="E-mail",background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=100,height=20)
tb_email=Entry(app)
tb_email.place(x=10,y=130,width=300,height=20)

Label(app,text="Obs",background="#dde",foreground="#009",anchor=W).place(x=10,y=160,width=100,height=20)
tb_obs=Text(app)#caixa de texto de várias linhas
tb_obs.place(x=10,y=180,width=300,height=80)

Button(app,text="Gravar", command=gravarDados).place(x=10,y=270,width=100,height=20)

app.mainloop()#gera uma janela