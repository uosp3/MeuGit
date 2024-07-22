import pyautogui
import time

pyautogui.PAUSE = 1 #pausa a cada comando

pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
#print(pyautogui.size())
time.sleep(2)

link = "https://gshow.globo.com/realities/bbb/bbb-24/voto-da-torcida/votacao/voto-da-torcida-quem-voce-quer-eliminar-do-bbb-24-h0Hsk3SKbB.ghtml"

pyautogui.click(x=197, y=60)
pyautogui.write(link)
pyautogui.press("enter")
votou=0
Conta=0
for v in range(2000):
    #espera="."
    espera=None   
    while espera == None:
        if Conta>10:
            pyautogui.click(x=197, y=60)
            pyautogui.write(link)
            pyautogui.press("enter")
        try:
            #time.sleep(2)     
            espera=pyautogui.locateCenterOnScreen("voto.png", grayscale=False)        
            print(v)
            pyautogui.click(espera)
            print("Achei escolhido(a)")        
        except:
            Conta+=1
            pyautogui.press("f5")       
            print(f"Erro na escolha. Conta = {Conta}") 

    espera=None
    Conta=0       
    while espera==None:
        try:
            #time.sleep(2)
            processando=None
            espera=pyautogui.locateCenterOnScreen("caixa.png", grayscale=False)               
            pyautogui.click(espera)
            print("Achei captcha")
            time.sleep(2)
            try:
                processando=pyautogui.locateCenterOnScreen("processando.png", grayscale=False) 
                print("Achei processando...")
                while processando!=None:
                    processando=pyautogui.locateCenterOnScreen("processando.png", grayscale=False)
            except:
                processando=None
                print(processando)                      
        except:
            print("Erro no captcha") 
            pyautogui.press("f5")
            break             

    espera=None 
    Conta=0   
    while espera==None:
            if Conta>6:
                pyautogui.press("f5")
                break
            try:                
                time.sleep(1) 
                espera=pyautogui.locateCenterOnScreen("repetev.png", grayscale=False)                           
                votou+=1
                print(f"{votou} Voto registrado")
                pyautogui.press("f5")                             
            except:
                Conta+=1
                print(f"Processando... = {Conta}")
                if processando==None:
                    Conta=7