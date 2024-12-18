# Meta caracteres: ^ $ ( )
# * 0 ou n = vale para qq coisa, mesmo que não exista.
# + 1 ou n = vale para qq coisa à esquerda do quantificador.
# ? 0 ou 1
import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
'''

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))  # pega todo o texto, sem separar
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))  # pega o texto por partes
