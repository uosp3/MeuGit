from tkinter import * #https://www.youtube.com/watch?v=GNlDce4WwcI&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=71
from tkinter import ttk

def imprimirEsporte():
    ve=cb_esportes.get()
    print("Esporte "+ve)

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

listaEsportes=["Futebol","Volei","Basquete"]

lb_esportes=Label(app,text="Esportes")
lb_esportes.pack()

cb_esportes=ttk.Combobox(app,values=listaEsportes)
cb_esportes.set("Selecione um esporte")
cb_esportes.pack()

btn_esporte=Button(app,text="Esporte Selecionado",command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()