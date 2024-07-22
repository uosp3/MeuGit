#https://www.youtube.com/watch?v=H6D8EFSGml0&list=PLOQgLBuj2-3LqnMYKZZgzeC7CKCPF375B&index=9
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

def find_by_text(browser, tag, text):
    #encontra o elemento com o texto 'text'
    #Argumentos:
        # navegador = instancia o browser
        # texto = conteudo que deve estar na tag
        # tag = tag onde o texto será procurado
    elementos = browser.find_elements(By.TAG_NAME, tag) #lista
    for elemento in elementos:
        if elemento.text == text:
            return elemento

browser = Chrome()

browser.get("http://selenium.dunossauro.live/aula_04_b.html")
#https://gshow.globo.com/realities/bbb/bbb-24/voto-da-torcida/votacao/voto-da-torcida-quem-voce-quer-eliminar-do-bbb-24-h0Hsk3SKbB.ghtml

nomes_das_caixas = ['um','dois','tres','quatro']

for nome in nomes_das_caixas:
    sleep(.5)
    find_by_text(browser, 'div', nome).click()

for nome in nomes_das_caixas:
    sleep(.5)
    browser.back()

for nome in nomes_das_caixas:
    sleep(.5)
    browser.forward()

input("Espera")

# parei em 1:03:30