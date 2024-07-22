'''
Se você precisa lidar com a verificação em duas etapas do Google,
onde o usuário precisa fornecer um código de verificação adicional após o
login inicial, você pode seguir alguns passos adicionais para integrar isso ao
seu script Selenium. Aqui está uma abordagem geral de como você pode
fazer isso:

1. **Realizar o login inicial:**
   - Utilize o Selenium para preencher o formulário de login do Google com seu
   usuário e senha.
   - Envie o formulário para efetuar o login.

2. **Lidar com a verificação em duas etapas:**
   - Após o login inicial, o Google geralmente solicita um código de
   verificação enviado por SMS, gerado por aplicativo autenticador ou
   por e-mail.
   - Para capturar este código, você precisará acessar o método pelo qual ele é
   fornecido (por exemplo, SMS, e-mail, aplicativo de autenticação).

3. **Inserir o código de verificação:**
   - Automatize a entrada do código de verificação no campo apropriado na
     página do Google.

Aqui está um exemplo simplificado de como você pode ajustar seu script para
 lidar com a verificação em duas etapas usando Selenium em Python:

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path  # meu


import os
from dotenv import load_dotenv
load_dotenv()
# print(os.getenv('SG'))


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent  # meu
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = str(ROOT_FOLDER / 'chromedriver.exe')  # meu

# Caminho para o executável do ChromeDriver
chrome_driver_path = CHROME_DRIVER_PATH

# Configuração das opções do Chrome
chrome_options = webdriver.ChromeOptions()

# Configuração para não usar o modo anônimo
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("detach", True)  # não fechar o naveg.
# Crie uma instância do WebDriver com as opções configuradas
driver = webdriver.Chrome(service=Service(
    chrome_driver_path), options=chrome_options)

# Abra a página de login do Google
driver.get('https://accounts.google.com')

# Encontre e preencha o campo de e-mail
email_input = driver.find_element(By.ID, 'identifierId')
email_input.send_keys('edson_g_santos@yahoo.com.br')

# Clique no botão "Próxima"
next_button = driver.find_element(By.ID, 'identifierNext')
next_button.click()

# Aguarde a página de senha carregar e preencha o campo de senha
WebDriverWait(driver, 10).until(EC.presence_of_element_located((
    By.NAME, 'Passwd')))
password_input = driver.find_element(By.NAME, 'Passwd')
password_input.send_keys(str(os.getenv('SG')))

# Clique no botão "Próxima" para fazer login
password_next_button = driver.find_element(By.ID, 'passwordNext')
password_next_button.click()

# Aguarde a página de verificação em duas etapas (se aplicável)
try:
    # Verifique se um determinado texto aparece na tela
    texto_especifico = "Toque em "
    # O texto que você está procurando
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
        (By.TAG_NAME, 'body'), texto_especifico))

    # Localize o elemento que contém o texto específico e clique nele
    elemento = driver.find_element(
        By.XPATH, f"//*[contains(text(), '{texto_especifico}')]")
    elemento.click()

except Exception as e:
    print(
        "Não foi possível encontrar ou clicar no"
        " elemento com o texto específico:", e)
# Aguarde até que um elemento específico apareça após o login
input("Perai....")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'backupCodePin'))
    )
    # Aguarde a página de código carregar e preencha o campo de código
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.ID, 'backupCodePin')))
    codigo_pin = driver.find_element(By.ID, 'backupCodePin')
    codigo_pin.send_keys(str(os.getenv('CG')))
    codigo_pin.send_keys(Keys.RETURN)
    print("Login realizado com sucesso!")
    # Agora você está logado e pode navegar para outras páginas ou realizar
    # outras ações necessárias
except TimeoutError:
    print("Timeout esperando pelo elemento de boas-vindas")


# Quando terminar, feche o navegador
# driver.quit()
"""

**Explicação adicional:**

- **Identificação do campo de código de verificação:** O código acima verifica
 se existe um campo específico onde o código de verificação é inserido.
 Isso pode variar dependendo do método escolhido para receber o código (SMS,
 e-mail, etc.). O exemplo assume que o campo tem o ID
 `'idvPreregisteredPhonePin'` e o botão de envio do código tem o ID
   `'idvPreregisteredPhoneNext'`. Você precisará ajustar isso com base
     na forma como você recebe o código de verificação.

- **Espera explícita:** O uso de `WebDriverWait` com
`EC.presence_of_element_located` garante que o Selenium espere até que o
elemento (por exemplo, o campo de código de verificação) esteja presente
na página antes de tentar interagir com ele.

- **Tratamento de exceções:** Inclui um tratamento básico de exceções para
 lidar com situações em que o campo de código de verificação não é encontrado
   ou ocorre um timeout esperando pelo elemento de boas-vindas após o login.

Certifique-se de ajustar os IDs e a lógica de espera para se adequar à página
 de login do Google e ao método específico de verificação em duas etapas que
   você está enfrentando (SMS, e-mail, aplicativo de autenticação, etc.). Isso
     deve permitir que seu script Selenium realize o login completo, incluindo
       a verificação em duas etapas, de maneira automatizada.
"""
