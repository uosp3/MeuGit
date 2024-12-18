# Meta caracteres: ^ $ ( )
# + 1 ou n = vale para qq coisa à esquerda do quantificador.
# ? 0 ou 1

# ()  \1  ====> o grupo e o retrovisor para acessar o grupo
# () () \1 \2
# (()) () \1 \2 \3
# para saber a qual grupo conta as aberturas dos parênteses.
import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

pprint(re.findall(r'(<([pdiv]{1,3})>.*?<\/[pdiv]{1,3}>)', texto))
tags = re.findall(r'(<([pdiv]{1,3})>(.*?)<\/[pdiv]{1,3}>)', texto)
print('.'*20)
for tag in tags:
    print(tag)
print('-'*20)
for tag in tags:
    um, dois, tres = tag  # desempacotou? em cada variável entra uma parte da expressão que foi fatiada de acorto com os parênteses (grupos).
    print(tres)  # pega o conteúdo das tags
print('*'*20)
tags = re.findall(r'<([pdiv]{1,3})>(?:.+?)<\/\1>', texto)
# ?: faz com que o grupo não seja salvo.
print(tags)

cpf = '447.715.846-27'
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))
print('\ / '*20)
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))