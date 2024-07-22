#https://www.youtube.com/watch?v=SkMATionZTQ&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=63
from tkinter import *
def imprimirEsporte():
    ve=vesporte.get()#pega o value do esporte selecionado.
    if ve== "Futebol":
        print("Esporte Futebol")
    elif ve== "Volei":
        print("Esporte Vôlei")
    elif ve== "Basquete":
        print("Esporte Basquete")
    else:
        print("Selecione um esporte")

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

listaEsportes=["Futebol", "Volei", "Basquete"]

vesporte=StringVar()#define o grupo do radiobuton
vesporte.set(listaEsportes[0])#define o esporte padrão da lista

bl_esportes=Label(app,text="Esportes")
bl_esportes.pack()

op_esportes=OptionMenu(app,vesporte,*listaEsportes)# o * indica que serão usados todos os elementos da lista
op_esportes.pack()

btn_esporte=Button(app,text="Esporte selecionado", command=imprimirEsporte)
btn_esporte.pack()


app.mainloop()