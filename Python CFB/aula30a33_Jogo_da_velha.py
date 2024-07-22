#https://www.youtube.com/watch?v=AhO-KN_tXSM&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=30
# caso vcs não tenha o "colorama" instalado, vai no terminal e escreva "pip install colorama"
import os
import random
from colorama import Fore, Back, Style
jogarNovamente="s"
jogadas=0
quemJoga=2 #1=cpu........2=usuario(jogador)
maxJogadas=9
vit="n"
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
def tela():
    global velha #é facultativo o global
    global jogadas #é facultativo o global
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] +" | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] +" | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] +" | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: ", Fore.GREEN, jogadas, Fore.RESET) #Reset para evitar que a sequencia fique na mesma cor.

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:        
        try:
            l=int(input("Linha...: "))
            c=int(input("Coluna..: "))
            while velha[l][c]!=" ": 
                l=int(input("Linha...: "))               
                c=int(input("Coluna..: "))
            velha[l][c]="X"              
            quemJoga=1
            jogadas+=1
        except:
            print("Jogada invalida")
            os.system("pause")
            #vit="n"

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==1 and jogadas<maxJogadas:
        l=random.randrange(0,3)#sorteia número entre zero e dois, (3)não conta.
        c=random.randrange(0,3)
        while velha[l][c]!= " ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        jogadas+=1
        quemJoga=2

def verificarVitoria():
    global velha
    vitoria="n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="n" 
        #verificar linas
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            il+=1
        if(vitoria!="n"):
            break
        #verificar colunas
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(velha[il][ic]==s):
                    soma+=1
                il+=1
            if(soma==3):
                vitoria=s
                break
            ic+=1
        if(vitoria!="n"):
            break
        #verifica diagonal 1
        soma=0
        idiag=0
        while idiag<3:
            if(velha[idiag][idiag]==s):
                soma+=1
            idiag+=1
        if(soma==3):
            vitoria=s
            break 
        #verifica diagonal 2
        soma=0
        idiagl=0
        idiagc=2
        while idiagc>=00:
            if(velha[idiagl][idiagc]==s):
                soma+=1
            idiagl+=1
            idiagc-=1
        if(soma==3):
            vitoria=s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas=0
    quemJoga=2 #1=cpu........2=usuario(jogador)
    maxJogadas=9
    vit="n"
    velha=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]           

while(jogarNovamente=="s" or jogarNovamente=="S"):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit=verificarVitoria()
        if(vit!="n") or (jogadas>=maxJogadas):
            break
    
    print("************************************")
    print(Fore.RED, "FIM DE JOGO", Fore.YELLOW)
    if(vit=="X" or vit=="O"):
        print("Resultado: Jogador ", vit, " venceu")
    else:
        print("Resutado: Empate")
    jogarNovamente=input(Fore.BLUE + "Jogar Novamente? [s/n]: " + Fore.RESET)
    redefinir()