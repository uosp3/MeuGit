# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34692280#questions/19560002
# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')