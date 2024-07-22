import aula34_canal as cn

cn.canal_nome()

#pode ser feita a importação de apenas parte do conteúdo de aula34_canal, fica assim:
from aula34_canal import jogador
print(cn.jogador["nome"])

#para saber o que tem em aula34_canal basta fazer um dir, assim:
res=dir(cn)
print(res)
