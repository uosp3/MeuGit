#https://www.youtube.com/watch?v=H6D8EFSGml0&list=PLOQgLBuj2-3LqnMYKZZgzeC7CKCPF375B&index=9
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url='http://selenium.dunossauro.live/aula_04_a.html'
navegador = Chrome()
navegador.get(url)
sleep(2)

ul = navegador.find_element(By.TAG_NAME,'ul')#pega a primeira "ul"
li=ul.find_elements(By.TAG_NAME,'li')#pega os "li" da primeira "ul"
a=li[0].find_elements(By.TAG_NAME,'a') #pega a primeira 'a' da 'li'

a[0].click()  
espera=input("espera")