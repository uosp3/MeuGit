# Meta caracteres:
# ^ --> começa com
# $ --> termina com
# [^a-z] --> negação (não pode conter nada entre a e z)

import re

cpf = '447.715.846-27'
print(re.findall(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$', cpf))
print(re.findall(r'[^a-z]+', cpf))
