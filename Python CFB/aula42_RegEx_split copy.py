import re #RegEx

texto="Curso de Python do CFB Cursos, canal do youtube"

res=re.split(" ", texto)#pesquisa algo dentro de outro algo e retorna os pedaços gerados a partir do que foi pesquisado.(no exemplo pode se usar "\s" para indicar a busca por espaço.)

print(res)
print(res[2])
for t in res:
    print(t)