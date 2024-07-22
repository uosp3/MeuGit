from sys import path

from aula99_package.modulo import soma_do_modulo
import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import *  # má pratica
import aula99_package

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula99_package.modulo.soma_do_modulo(3, 2))
print(modulo.soma_do_modulo(3, 7))
print(variavel)
# print(nova_variavel) # para que essa linha funcione é necessário que
# 'nova_variável' esteja dentro de __all__ la no arquivo aula99_package.

print(aula99_package.dobra(2))
