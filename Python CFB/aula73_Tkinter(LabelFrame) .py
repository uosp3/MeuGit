from tkinter import * #https://www.youtube.com/watch?v=lUN2RFOykX4&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=73

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

lb_esportes=LabelFrame(app,text="Esportes",borderwidth=1,relief="solid")
lb_esportes.place(x=10,y=10,width=300,height=100)

le1=Label(lb_esportes,text="Futebol")
le1.pack()

le2=Label(lb_esportes,text="Volei")
le2.pack()

le3=Label(lb_esportes,text="Basquete")
le3.pack()

app.mainloop()