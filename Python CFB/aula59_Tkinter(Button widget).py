#https://www.youtube.com/watch?v=GsKbhAxL4SM&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=60
from tkinter import *
import os

c=os.path.dirname(__file__)#pega o caminho deste arquivo
nomeArquivo=c+"\\aula59_arquivoGerado.txt"

def gravarDados():
    arquivo=open(nomeArquivo,"a") #abre o arquivo para anexar
    arquivo.write("Nome....:%s" % vnome.get()) #%s indica que vai entrar uma string. A variável 'vnome' ta associado a um componente 'Entry' e 'get()' retorna o texto que foi digitado no componente.
    arquivo.write("\nTelefone:%s" % vfone.get())
    arquivo.write("\nE-mail..:%s" % vemail.get())
    arquivo.write("\nObs.....:%s" % vobs.get("1.0",END))#neste caso o campo é um 'text' tem que informar onde deve começar e onde deve parar.
    arquivo.write("\n")
    arquivo.close()

app=Tk()
app.title("CFB Cursos")#titulo da janela
app.geometry("500x300")#tamanho da janela
app.configure(background="#dde")#cor de fundo

Label(app,text="Nome",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)#cria um label dentro do app, cor de fundo cor da letra e ponto cardeal  
#place faz o label aparecer, onde aparecer e de que tamanho.
vnome=Entry(app)#caixa de texto de uma linha
vnome.place(x=10,y=30,width=200,height=20)

Label(app,text="Telefone",background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=100,height=20)
vfone=Entry(app)
vfone.place(x=10,y=80,width=100,height=20)

Label(app,text="E-mail",background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=100,height=20)
vemail=Entry(app)
vemail.place(x=10,y=130,width=300,height=20)

Label(app,text="Obs",background="#dde",foreground="#009",anchor=W).place(x=10,y=160,width=100,height=20)
vobs=Text(app)#caixa de texto de várias linhas
vobs.place(x=10,y=180,width=300,height=80)

Button(app,text="Gravar", command=gravarDados).place(x=10,y=270,width=100,height=20)

app.mainloop()#gera uma janela