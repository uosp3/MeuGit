# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35059056#questions
# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 2134


call1 = CallMe('33999233433')
retorno = call1('Edson')
print(retorno)