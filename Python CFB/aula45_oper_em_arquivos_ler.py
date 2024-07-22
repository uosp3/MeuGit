#https://www.youtube.com/watch?v=5fSKfl8lI1w&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=45
import re
nome="aula44_teste.txt"
f=open("E:/Cursos/Tudo/Python/"+ nome,"rt") #caminho do arquivo a ser aberto

res=re.sub(" ","-",f.readline())
f.seek(0)#move o cursor para a posição zero.
print(f.read()) #o parâmetro indica a quantidade de caracteres a serem lidos, para tudo deixar sem parâmetro.
f.seek(0)
print("\nImpresso pelo readline().................")
print(f.readline())#lê uma linha
f.seek(0)
print("Impresso pelo loop.................")
for l in f:#loop para ler todas as linhas
    print(l)

f.close() #fechar o arquivo depois de usado.

print("\nImpresso pelo res trocando espaço por traço........")
print(res)