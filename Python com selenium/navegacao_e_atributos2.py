#https://www.youtube.com/watch?v=H6D8EFSGml0&list=PLOQgLBuj2-3LqnMYKZZgzeC7CKCPF375B&index=9
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

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
        
def find_by_href(browser, link):
    #encontra o elemento 'a' com o link 'link'
    #Argumentos:
        # navegador = instancia o browser
        # link = link que será procurado em todas as tag 'a'
    elementos = browser.find_elements(By.TAG_NAME, 'a') #lista
    for elemento in elementos:
        if link in elemento.get_attribute('href'):   
            return elemento     

browser = Chrome()

browser.get("http://selenium.dunossauro.live/aula_04_a.html")

elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')
elemento_ddg2 = find_by_href(browser, 'ddg')

print(elemento_ddg2.text)
print(elemento_ddg2.get_attribute("href"))
input("Espera")

