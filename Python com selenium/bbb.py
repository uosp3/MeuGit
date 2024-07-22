import pyautogui
import time

pyautogui.PAUSE = 1 #pausa a cada comando

pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
time.sleep(2)

link = "https://gshow.globo.com/realities/bbb/bbb-24/voto-da-torcida/votacao/voto-da-torcida-quem-voce-quer-eliminar-do-bbb-24-h0Hsk3SKbB.ghtml"

pyautogui.click(x=197, y=60)
pyautogui.write(link)
pyautogui.press("enter")

for v in range(2000):
    espera="."
    while espera==".":
        try:
            time.sleep(2)     
            espera=pyautogui.locateCenterOnScreen("voto.png", grayscale=False)        
            print(v)
            pyautogui.click(espera)
            print(espera)        
        except:
            print("Except voto")

    espera="."
    Conta=0       
    while espera==".":
        if Conta>6:
            pyautogui.press("f5")
            break        
        try:
            time.sleep(2)
            espera=pyautogui.locateCenterOnScreen("caixa.png", grayscale=False)    
            pyautogui.click(espera)
        except:
            print(f"Except captcha. Conta = {Conta}")
            Conta+=1       

    espera="." 
    Conta=0   
    while espera==".":
            if Conta>6:
                pyautogui.press("f5")
                break
            try:
                time.sleep(2) 
                espera=pyautogui.locateCenterOnScreen("repete.png", grayscale=False)                           
                print(f"Repete? Espera = {espera}")
                pyautogui.press("f5")                             
            except:
                print(f"Espera = {espera} conta = {Conta}") 
                Conta+=1      