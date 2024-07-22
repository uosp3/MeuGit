import urllib.request #https://www.youtube.com/watch?v=wjoI4EegrBI&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=85
import os

pagina=urllib.request.urlopen("https://www.duolingo.com/")#carrega a pagina
texto=pagina.read().decode("utf8")#converte para utf8

#dado=texto[0:21]#pega uma referencia específica na pagina

pos_ini=pagina.find("jeito")

print(pos_ini)