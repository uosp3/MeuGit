from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas #pip install reportlab
from reportlab.lib.pagesizes import A4
import os

def mp(mm):#converter milímetros para pontos
    return mm/0.352777

pastaApp=os.path.dirname(__file__)

def criarPDF():
    try:
        cnv=canvas.Canvas(pastaApp+"\\cfbcursos.pdf",pagesize=A4)
        cnv.drawImage(pastaApp+"\\logo.gif",mp(0),mp(207))
        cnv.circle(mp(100),mp(100),mp(25))# x, y e raio
        cnv.drawString(mp(100),mp(100),"CFB Cursos - PDF") #posição do texto (x y)
        cnv.save()
    except:
        messagebox.showinfo(title="Erro",message="Verifique se o arquivo ja existe e se está aberto")

app=Tk()
app.title("CFB Cursos")
app.geometry("600x450")

btn_criarPDF=Button(app,text="Criar PDF", command=criarPDF)
btn_criarPDF.pack(side='left',padx=10)

app.mainloop()