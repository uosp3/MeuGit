#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/15128580#questions/10067444
# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #decorator, faz com que possa chamar a classe sem o 'self', mas é preciso receber um parâmetro, no caso a própria classe(ao molde não á instância) geralmente chamado 'cls'
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod #metodo que cria um objeto com alguma coisa arbitraria ou alguma lógica
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()