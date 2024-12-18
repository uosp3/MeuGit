# Meta caracteres: ^ $ ( )
# * 0 ou n = vale para qq coisa, mesmo que não exista.
# + 1 ou n = vale para qq coisa à esquerda do quantificador.
# ? 0 ou 1
# {n}
    # assim: {10} especificamente 10
# {min, max} 
    # assim: {10,} 10 ou mais
    # assim: {,10} de zero a 10
    # assim: {5,10} de 5 a 10
# ()+ [a-zA-z]+
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãoooooooo, o café tá prontinho aqui. Veeemm"!
jã
'''

print(re.findall(r'jo+ão+', texto, flags=re.I)) # ignorecase
print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I)) # substitue o texto encontrado pelo texto que foi passado 'Felipe"
print(re.sub(r'jo*ão*', 'Felipe', texto, flags=re.I)) # substitue o texto encontrado pelo texto que foi passado 'Felipe"
print('...........')
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I)) # substitue 1 ou mais
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

texto2 = 'João ama ser amado'
print(re.findall(r'ama[do]{2}', texto2))