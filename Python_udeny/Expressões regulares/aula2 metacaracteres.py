# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | = ou
# . = qualquer caractere (exceto quebra de linha)
# [] = conjunto de caracteres
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
'''

print(re.findall(r'João|Maria', texto)) # |
print(re.findall(r'J...', texto)) # .
print(re.findall(r'[jJ]oão', texto)) # []
print(re.findall(r'[a-zA-Z0-9]aria', texto)) # [range]
print(re.findall(r'jOãO', texto, flags=re.I)) # ignorecase

