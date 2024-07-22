from tkinter import * #https://www.youtube.com/watch?v=FQ1exJhqvo0&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=76
from tkinter import ttk

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

nb=ttk.Notebook(app)#cria um notebook dentro do app
nb.place(x=5,y=0,width=490,height=290)

tb1=Frame(nb)#Cria um frame
tb2=Frame(nb)

nb.add(tb1,text="Cursos")#adiciona o frame ao notebook
nb.add(tb2,text="Canal")

lb1=Label(tb1,text="Curos de Python")
lb1.pack()
lb2=Label(tb1,text="Curos de ReactNative")
lb2.pack()

lb3=Label(tb2,text="Youtube.com/cfbcursos")
lb3.pack()

app.mainloop()