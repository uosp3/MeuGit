# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35467708#questions/19367964
# secrets gera números aleatórios seguros
import secrets

import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
# as linhas abaixo pode ser colada no terminal para ver um exemplo
# de código gerado aleatoriamente.
# python -c "import string as s;from secrets import SystemRandom as Sr;
# print(''.join(Sr().choices(s.ascii_letters + s.punctuation +
# s.digits,k=12)))"

random = secrets.SystemRandom()  # faz o random se comportar como secrets

print(secrets.randbelow(100))  # gera nº aleatório até 100
print(secrets.choice([10, 11, 12]))  # escolhe um dos numeros aleatoriamente

# Funções:
# seed
#   -> NÃO FAZ NADA
random.seed(10)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(round(r_uniform, 2))

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)
print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))
