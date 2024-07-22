from tkinter import * #https://www.youtube.com/watch?v=chGCliVDYgU&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=77
from tkinter import ttk

def valBarra(m):
    cont=0
    etapas=m/100
    while cont<etapas:
        cont=cont+1
        i=0
        while i<1000000:
            i=i+1
        varBarra.set(cont)
        app.update()

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

varBarra=DoubleVar()#variável a ser usada na progressbar
varBarra.set(0)#valor inicial da barra

pb=ttk.Progressbar(app,variable=varBarra,maximum=100)
pb.place(x=50,y=0,width=400,height=40)

btn=Button(app,text="Definir Barra",command=lambda:valBarra(10000))
btn.place(x=0,y=50,width=100,height=40)

app.mainloop()