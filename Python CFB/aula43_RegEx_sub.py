import re #RegEx

texto="Curso de Python do CFB Cursos, canal do youtube"

res=re.sub("Python","JavaScript", texto)#pesquisa um dado e substitui por outro.

print(res)
