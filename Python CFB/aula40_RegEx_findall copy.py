import re #RegEx

texto="Curso de Python do CFB Cursos, canal do youtube"

pesq=input("Pesquisar: ")

res=re.findall(pesq, texto)#pesquisa algo dentro de outro algo
qtde=len(res) #quantidade de elementos encontrados.

print(res)
print("Qtde: ",qtde)