from tkinter import * #https://www.youtube.com/watch?v=uk40wvI8Y-k&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=74

def imprimirEsporte():
    print("Esporte: "+lb_esportes.get(ACTIVE))

def addEsporte():
    lb_esportes.insert(END,vnovoesporte.get())

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

listaEsportes=["Futebol","Volei","Basquete"]

lb_esportes=Listbox(app)
for esportes in listaEsportes:
    lb_esportes.insert(END,esportes)
lb_esportes.pack()

btn_esporte=Button(app,text="Imprimir Esporte", command=imprimirEsporte)
btn_esporte.pack()

vnovoesporte=Entry(app)
vnovoesporte.pack()

btn_inseriresporte=Button(app,text="Adicionar Esporte", command=addEsporte)
btn_inseriresporte.pack()

app.mainloop()