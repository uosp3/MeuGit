# https://googlechromelabs.github.io/chrome-for-testing/
# link para baixa o chromedriver

# código para atualizar o chromedriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
