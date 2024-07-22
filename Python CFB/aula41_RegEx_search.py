import re #RegEx

texto="Curso de Python do CFB Cursos, canal do youtube"

res=re.search("Python", texto)#pesquisa algo dentro de outro algo e retorna a primeira posição.

if(res != None):
    pi=res.start()#posição inicial
    pf=res.end()#posição final
    tam=pf-pi #tamanho
    print(res.start())
    print(res.end())
    print(tam)
else:
    print("Nao encontrado")