#https://www.youtube.com/watch?v=J5HkAUNCIVM&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=65
from tkinter import *
from tkinter import messagebox
def mostrarMsg(tipomsg,msg):
    if(tipomsg=="1"):
        messagebox.showinfo(title="CFB Cursos", message=msg)
    elif(tipomsg=="2"):
        messagebox.showwarning(title="CFB Cursos", message=msg)
    elif(tipomsg=="3"):
        messagebox.showerror(title="CFB Cursos", message=msg)

def resetarTB():
    res=messagebox.askyesno("Resetar", "Cofirma reset do textbox?")
    #askquestion - faz o mesmo que yesno
    #askokcancel - Retorna (True, False)
    #askretrycancel - Retorna (True, False)
    #askyesnocancel - Retorna SIM, NÃO e CANELAR (True, False, None)
    
    if(res==True):
        tb_num.delete(0,END)#limpa o textbox
        tb_num.insert(0,"1")#atribui novo valor ao texbox

vmsg="Curso de Python/Tkinter"

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")

vnum_cxtexto=StringVar()#armazena o resultado da caixa de texto 'Entry'

Label(app,text="Tipo de cx(1,2 ou 3)").pack()
tb_num=Entry(app,textvariable=vnum_cxtexto)
vnum_cxtexto.set("1")#define o valor padrão da caixa de texto
tb_num.pack()

btn_msg=Button(app,text="Mostrar mensagem",command=lambda:mostrarMsg(vnum_cxtexto.get(),vmsg))
btn_msg.pack()

btn_reset=Button(app,text="Resetar Textbox",command=resetarTB)
btn_reset.pack()

app.mainloop()