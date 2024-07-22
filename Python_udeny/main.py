from sys import path
from aula99_package.modulo import soma_do_modulo
print(__name__)
print(*path, sep='\n')  # * para desempacotar/expandir a lista
print(soma_do_modulo(1, 2))
