# Atributos de classe
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34845012#questions
import datetime


class Pessoa:
    ano_atual = datetime.datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 63)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
