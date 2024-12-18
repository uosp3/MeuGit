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

print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))  # pega tudo do texto, palavras acentuadas, maiúsculas, minúsculas e números.
print('*'*30)
print(re.findall(r'\w+', texto))  # atalho para fazer o meso que a linha
print('*'*30)
print(re.findall(r'\d+', texto))  # pega so números
print('*'*30)
print(re.findall(r'\s+', texto))  # pega espaços e quebras de linha
print('*'*30)
print(re.findall(r'\bf\w+', texto))  # pega o que começo com...
print('*'*30)
print(re.findall(r'\w+e\b', texto))  # pega o que termina com...
print('*'*30)
print(re.findall(r'\b\w{4}\b', texto))  # pega o que tiver 4 letras
print('*'*30)
print(re.findall(r'quec\B', texto))  # pega o que tiver o texto, em qualquer parte da palavra

print('*'*30)

# re.A -> ASCII
# re.I -> ignore
# re.M -> multiline -> ^ (começa com) $ (termina com)
# re.S -> DotAll \n

texto = '''
131.768.460-53 ABC
055.123.060-50 DEF
955.123.060-90
'''
print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))

texto2 = 'O João gosta de folia \n E adora ser amado'
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S ))