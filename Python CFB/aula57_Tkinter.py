#https://www.youtube.com/watch?v=gcpy2syshXA&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=57
from tkinter import *

app=Tk()
app.title("CFB Cursos")#titulo da janela
app.geometry("500x300")#tamanho da janela
app.configure(background="#008")#cor de fundo

txt1=Label(app,text="Curso de Python",background="#ff0",foreground="#000")#cria um label dentro do app, fundo amarelo e letra preta.
txt1.place(x=10,y=10,width=150,height=30)#faz o label aparecer, onde aparecer e de que tamanho.

vtxt="Módulo Tkinter"
vbg="#ff0"
vfg="#000"
txt2=Label(app,text=vtxt,bg=vbg,fg=vfg)#nesse caso o label usou variáveis
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=X,expand=True)#pack funciona como o place so que em um container.

app.mainloop()#gera uma janela