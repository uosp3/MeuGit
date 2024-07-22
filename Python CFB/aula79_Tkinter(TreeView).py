from tkinter import * #https://www.youtube.com/watch?v=kScAALk2Awc&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=79
from tkinter import ttk

app=Tk()
app.title("CFB Cursos")
app.geometry("600x300")

listaNomes=[['0','Edson','2345'],['1','Laine','4556'],['2','Gomes','4656']]

tv=ttk.Treeview(app,columns=('id','nome','fone'),show='headings') #headings=cabeçalho
tv.column('id',minwidth=0,width=50)#define o tamanho da coluna
tv.column('nome',minwidth=0,width=250)
tv.column('fone',minwidth=0,width=100)
tv.heading('id',text="ID")#define o nome dos cabeçalhos
tv.heading('nome',text="NOME")
tv.heading('fone',text="TELEFONE")
tv.pack()

for (i,n,f) in listaNomes:
    tv.insert('','end',values=(i,n,f))

app.mainloop()