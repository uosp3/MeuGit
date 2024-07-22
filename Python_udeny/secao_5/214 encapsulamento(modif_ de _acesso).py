#https://github.com/luizomf/cursopython2023/blob/edf4941ffc5a52be6ba55c898c0daf4557d43998/aula133.py
# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é private'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__private)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
# print(f.public)
print(f.metodo_publico())
#print(f.__metodo_private())  #essa linha da erro, pois o método é privado e não pode ser acessado fora da classe. Uma forma de usar seria conforme a linha abaixo, mas isso não recomendado pela comunidade.
print(f._Foo__metodo_private())

