#https://www.youtube.com/watch?v=SkMATionZTQ&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=63
from tkinter import *

def imprimirEsporte():
    ve=vesporte.get()#pega o value do esporte selecionado.
    if ve== "f":
        print("Esporte Futebol")
    elif ve== "v":
        print("Esporte Vôlei")
    elif ve== "b":
        print("Esporte Basquete")
    else:
        print("Selecione um esporte")

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")
0
vesporte=IntVar()#define o grupo do radiobuton
vcor=IntVar()#define o grupo do radiobuton

bl_esportes=Label(app,text="Esportes")
bl_esportes.pack()

rb_futebol=Radiobutton(app,text="Futebol",value="f", variable=vesporte)
rb_futebol.pack()

rb_volei=Radiobutton(app,text="Vôlei",value="v", variable=vesporte)
rb_volei.pack()

rb_basquete=Radiobutton(app,text="Basquete",value="b", variable=vesporte)
rb_basquete.pack()

rb_verde=Radiobutton(app,text="Verde",value="#0f0", variable=vcor)
rb_verde.pack()

rb_vermelho=Radiobutton(app,text="Vermelho",value="#0f00", variable=vcor)
rb_vermelho.pack()

btn_esporte=Button(app,text="Esporte selecionado", command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()