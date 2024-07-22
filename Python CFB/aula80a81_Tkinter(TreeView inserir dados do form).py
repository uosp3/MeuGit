from tkinter import * #https://www.youtube.com/watch?v=x4unDBA0AP8&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=80
from tkinter import ttk
from tkinter import messagebox

def inserir():
    if vid.get()=='' or vnome.get()=='' or vfone.get()=='':
        messagebox.showinfo(title="Erro",message="Digite todos os dados")
        return
    tv.insert('','end',values=(vid.get(),vnome.get(),vfone.get()))
    vid.delete(0,END)
    vnome.delete(0,END)
    vfone.delete(0,END)
    vid.focus()

def deletar():
    try:
        itemSelecionado=tv.selection()[0]#pega o elemento selecionado
        tv.delete(itemSelecionado)
    except:
        messagebox.showerror(title="Erro", message="Selecione um elemento a ser deletado")

def obter():
    try:
        itemSelecionado=tv.selection()[0]#pega o elemento selecionado
        valores=tv.item(itemSelecionado,"values")
        print("ID........:",valores[0])
        print("Nome......:",valores[1])
        print("Telefone..:",valores[2])
    except:
        messagebox.showerror(title="Erro", message="Selecione o elemento a ser mostrado")


app=Tk()
app.title("CFB Cursos")
app.geometry("413x320")

lbid=Label(app,text='ID')#, anchor='w') #anchor alinha/posição o elemento
vid=Entry(app)

lbnome=Label(app,text='Nome')#, anchor='w') #anchor alinha/posição o elemento
vnome=Entry(app)

lbfone=Label(app,text='Fone')#, anchor='w') #anchor alinha/posição o elemento
vfone=Entry(app)

tv=ttk.Treeview(app,columns=('id','nome','fone'),show='headings') #headings=cabeçalho
tv.column('id',minwidth=0,width=50)#define o tamanho da coluna
tv.column('nome',minwidth=0,width=250)
tv.column('fone',minwidth=0,width=100)
tv.heading('id',text="ID")#define o nome dos cabeçalhos
tv.heading('nome',text="NOME")
tv.heading('fone',text="TELEFONE")

btn_inserir=Button(app,text="Inserir",command=inserir)
btn_deletar=Button(app,text="Deletar",command=deletar)
btn_obter=Button(app,text="Obter",command=obter)

lbid.grid(column=0,row=0,sticky='w')
vid.grid(column=0,row=1)

lbnome.grid(column=1,row=0,sticky='w')
vnome.grid(column=1,row=1)

lbfone.grid(column=2,row=0,sticky='w')
vfone.grid(column=2,row=1)

tv.grid(column=0,row=3,columnspan=3,pady=5,padx=4)

btn_inserir.grid(column=0,row=4)
btn_deletar.grid(column=1,row=4)
btn_obter.grid(column=2,row=4)

#tv.insert('','end',values=(i,n,f))

app.mainloop()