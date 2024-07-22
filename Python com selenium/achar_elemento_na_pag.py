from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
url='https://curso-python-selenium.netlify.app/aula_03.html'
navegador = Chrome()
navegador.get(url)
time.sleep(5)

a=navegador.find_element(By.TAG_NAME,'a')

for click in range(1,11):
    a.click()    
    ps=navegador.find_elements(By.TAG_NAME,'p')
    print(f'Valor de p {ps[-1].text} valor do click: {click}')
    
a=input("espera")