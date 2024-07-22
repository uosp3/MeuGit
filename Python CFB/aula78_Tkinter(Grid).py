from tkinter import * #https://www.youtube.com/watch?v=fNGWp9G30aM&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=78

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

lb_canal=Label(app,text="CFB Cursos")
lb_nome=Label(app,text="Digite seu nome")
lb_idade=Label(app,text="Informe sua idade")

et_nome=Entry(app)
et_idade=Entry(app)

btn=Button(app,text="Youtube")

lb_canal.grid(column=0,row=0,columnspan=2, pady=15)#columnspan mescla as colunas e pad(x ou y) é o espaço ao lado do elemento

lb_nome.grid(column=0,row=1,sticky="w")#sticky é a posição no elemento pai
et_nome.grid(column=0,row=2,padx=5)

lb_idade.grid(column=1,row=1,sticky="w")#sticky é a posição no elemento pai
et_idade.grid(column=1,row=2,padx=5)

app.mainloop()