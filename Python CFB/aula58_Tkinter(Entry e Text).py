#https://www.youtube.com/watch?v=IjouwdFwsg0&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=58
from tkinter import *

app=Tk()
app.title("CFB Cursos")#titulo da janela
app.geometry("500x300")#tamanho da janela
app.configure(background="#dde")#cor de fundo

Label(app,text="Nome",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)#cria um label dentro do app, cor de fundo cor da letra e ponto cardeal  
#place faz o label aparecer, onde aparecer e de que tamanho.
vnome=Entry(app)#caixa de texto de uma linha
vnome.place(x=10,y=30,width=200,height=20)

Label(app,text="Telefone",background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=100,height=20)
vfone=Entry(app)
vfone.place(x=10,y=80,width=100,height=20)

Label(app,text="E-mail",background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=100,height=20)
vemail=Entry(app)
vemail.place(x=10,y=130,width=300,height=20)

Label(app,text="Obs",background="#dde",foreground="#009",anchor=W).place(x=10,y=160,width=100,height=20)
vobs=Text(app)#caixa de texto de várias linhas
vobs.place(x=10,y=180,width=300,height=80)

app.mainloop()#gera uma janela