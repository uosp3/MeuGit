nome="aula44_teste.txt"
f=open("E:/Cursos/Tudo/Python/"+ nome,"w") #caminho do arquivo a ser aberto
#r - Read(abre para leitura)
#a - append - anexar algo ao arquivo
#w - write(abre para escrita), se não existir será criado
#x - create(cria um arquivo)
#t - texto (pode ser omitido, é padrão.)
#b - binário

#se rodar duas vezes no modo "w" a segunda vez vai sobrepor à primeira, para evitar isto usar o parâmetro "a"

txt=input("Digito um texto para passar para o arquivo externo.")
f.write(txt+"\n")

f.close() #fechar o arquivo depois de usado.