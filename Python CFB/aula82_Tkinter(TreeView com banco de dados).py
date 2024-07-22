from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import aula82_banco as Banco

def popular():
    tv.delete(*tv.get_children())
    vquery="select * from tb_nomes order by id"
    linhas=Banco.dql(vquery)
    for i in linhas:
        tv.insert('','end',values=i)

def inserir():
    if vnome.get()=='' or vfone.get()=='':
        messagebox.showinfo(title="Erro", message="Digite todos os dados")
        return
    try:
        vquery="insert into tb_nomes (nome,fone) values ('"+vnome.get()+"','"+vfone.get()+"')"
        Banco.dml(vquery)
    except:
        messagebox.showinfo(title="Erro",message="Erro ao inserir")
        return
    popular()
    vnome.delete(0,END)
    vfone.delete(0,END)
    vnome.focus()

def deletar():
    vid=-1
    itemSelecionado=tv.selection()[0]
    valores=tv.item(itemSelecionado, "values")
    vid=valores[0]
    try:
        vquery="delete from tb_nomes where id="+vid
        Banco.dml(vquery)
    except:
        messagebox.showinfo(title="Erro",message="Erro ao deletar")
        return
    tv.delete(itemSelecionado)

def pesquisar():
    tv.delete(*tv.get_children())
    vquery="select * from tb_nomes where nome like '%"+vnomepesquisar.get()+"%'"
    linhas=Banco.dql(vquery)
    for i in linhas:
        tv.insert("","end",values=i)
    vnomepesquisar.delete(0,END)

app=Tk()
app.title("CFB Cursos")
app.geometry("600x450")

###########################
quadroGrid=LabelFrame(app,text="Contatos")
quadroGrid.pack(fill='both',expand='yes',padx=10,pady=10)

tv=ttk.Treeview(quadroGrid,columns=('id','nome','fone'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=250)
tv.column('fone',minwidth=0,width=100)
tv.heading('id',text="ID")
tv.heading('nome',text="NOME")
tv.heading('fone',text="TELEFONE")
tv.pack()
popular()

############################

quadroInserir=LabelFrame(app,text="Inserir Noves Contatos")
quadroInserir.pack(fill='both',expand='yes',padx=10,pady=10)

lbnome=Label(quadroInserir, text="Nome")
lbnome.pack(side='left')
vnome=Entry(quadroInserir)
vnome.pack(side="left",padx=10)
lbfone=Label(quadroInserir, text="Fome")
lbfone.pack(side='left')
vfone=Entry(quadroInserir)
vfone.pack(side="left",padx=10)
btn_inserir=Button(quadroInserir,text="Inserir",command=inserir)
btn_inserir.pack(side='left',padx=10)

##############################

quadroPesquisar=LabelFrame(app,text="Pesquisar Contatos")
quadroPesquisar.pack(fill='both',expand='yes',padx=10,pady=10)

lbid=Label(quadroPesquisar,text="Nome")
lbid.pack(side="left")
vnomepesquisar=Entry(quadroPesquisar)
vnomepesquisar.pack(side='left',padx=10)
btn_pesquisar=Button(quadroPesquisar,text="Pesquisar",command=pesquisar)
btn_pesquisar.pack(side='left',padx=10)  
btn_todos=Button(quadroPesquisar,text="Mostrar Todos", command=popular)
btn_todos.pack(side='left',padx=10)

app,mainloop()