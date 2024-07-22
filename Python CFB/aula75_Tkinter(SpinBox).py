from tkinter import * #https://www.youtube.com/watch?v=wSVXlrvlR5M&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=75

def ImpVal():
    print("Valor: "+sp_valores.get())

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

sp_valores=Spinbox(app,from_=0,to=10)#from e to é a faixa de valores
sp_valores.pack()
#outro tipo:
sp_valores2=Spinbox(app,values=(1,2,3,4,5))#values tb é a faixa de valores
sp_valores2.pack()

btn_valor=Button(app,text="Imprimir valor",command=ImpVal)
btn_valor.pack()

app.mainloop()