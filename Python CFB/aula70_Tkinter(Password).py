from tkinter import * #https://www.youtube.com/watch?v=aHtDVRQ_OdM&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=70

def impSenha():
    print("Senha digitada: "+vsenha.get())

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

vsenha=StringVar()

p_senha=Entry(app,textvariable=vsenha,show="*")
p_senha.pack()

btn_mostraSenha=Button(app,text="Imprimir Senha", command=impSenha)
btn_mostraSenha.pack()

app.mainloop()