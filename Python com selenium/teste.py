#https://www.youtube.com/watch?v=WzUPnQwSQyk
import requests
from bs4 import BeautifulSoup

link='https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar'

#a infomação abaixo, a partir de "Mozilla/5", é obtida no inspecionar site, opção network, headers, user-agent. Ela é necessárioa para "enganar" o sistema e ele nãosaber que a requisição está sendo feita por um código.Obs.:usar antes da requisição
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

requisicao=requests.get(link, headers=headers)

print(requisicao)#se a requisição deu certo = 200
#print(requisicao.text) #pega todoo conteudo do site

site=BeautifulSoup(requisicao.text,'html.parser')
#print(site.prettify()) #mostra todo o conteudo de forma mais organizada

titulo = site.find("title") #pega o título do site
#print(titulo)

pesquisa = site.find_all("input")#pega todos os input
#print(pesquisa[2])#printa o input 2
print(pesquisa[2]["value"])

pesquisa = site.find("span", class_="SwHCTb")
print(pesquisa["data-value"])
print(pesquisa.get_text())



