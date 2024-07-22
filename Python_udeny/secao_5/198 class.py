# https://www.youtube.com/watch?v=gomDSZaay3E&t=0s
# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    ...


p1 = Pessoa()
p1.nome = 'Luiz'  # type: ignore
p1.sobrenome = 'Otávio'  # type: ignore

p2 = Pessoa()
p2.nome = 'Maria'  # type: ignore
p2.sobrenome = 'Joana'  # type: ignore

print(p1.nome)  # type: ignore
print(p1.sobrenome)  # type: ignore

print(p2.nome)  # type: ignore
print(p2.sobrenome)  # type: ignore
