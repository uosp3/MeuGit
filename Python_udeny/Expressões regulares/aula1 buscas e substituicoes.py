# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
import re

# findall search sub
# compile

string = 'Este é um teste de expressões teste regulares.'
print(re.search(r'teste', string))  # encontra a 1ª ocorrencia
print(re.findall(r'teste', string))  # encontra a todas ocorrencia
print(re.sub(r'teste', 'ABCD', string))  # substitui o texto encontrado
print(re.sub(r'teste', 'ABCD', string, count=1))  # substitui o texto encontrado, apenas a primeira ocorrencia.


regexp = re.compile(r'teste')  # faz a mesma coisa so que não precisa ficar repetindo a expressão.
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))