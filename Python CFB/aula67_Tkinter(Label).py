#https://www.youtube.com/watch?v=9aV24EJMcxU&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=66
from tkinter import *
from tkinter import messagebox

def mostrarMsg():
    messagebox.showinfo(title="CFB Cursos", message="CFB Cursos, curso de Python/Tkinter")

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

vnum_cxtexto=StringVar()

fr_quadro1=Frame(app, borderwidth=1,relief="solid")
#bordas do frame - relief (flat, raised,sunken, solid)
fr_quadro1.place(x=10,y=10,width=300,height=100)

lb_tipo=Label(fr_quadro1,text="Tipo de cx(1,2 ou 3)")
lb_tipo.place(x=10,y=10)
tb_num=Entry(fr_quadro1,textvariable=vnum_cxtexto)
vnum_cxtexto.set("1")#define o valor padrão da caixa de texto
tb_num.place(x=10,y=30)

btn_msg=Button(fr_quadro1,text="Mostrar mensagem",command=mostrarMsg)
btn_msg.place(x=10,y=50)

fr_quadro2=Frame(app, borderwidth=1,relief="solid",background="#008")
fr_quadro2.place(x=10,y=120,width=300,height=100)

lb_canal=Label(fr_quadro2, text="CFB Cursos", background="#008",foreground="#fff",font=("Arial",15))
lb_canal.pack(side=LEFT,fill=X, expand=True)

app.mainloop()