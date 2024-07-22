# map, partial, GeneratorType e esgotamento de Iterators
"""
Map(): é uma função que aplica uma função a cada elemento de uma lista e retorna uma nova lista com os resultados.
Sintaxe: map(função, lista)
""" 
#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34736176#questions

from functools import partial #funcão que recebe uma função
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator): # so para printar...
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print_iter(produtos)

#opção com list comprehension = aumenta o valor em 10%
novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1, 2)} for p in produtos
]
print('opção com list comprehension = aumenta o valor em 10%')
print_iter(novos_produtos)


#outra opção, ainda com list comprehension, mesmo caso acima. Agora substituido (round(p['preco']*1.1, 2)) pela função 'aumentar_porcentagem'
def aumentar_porcentagem(valor, porcentagem): #função para aumentar o valor
    return round(valor * porcentagem, 2)
novos_produtos = [
    {**p, 'preco': aumentar_porcentagem(p['preco'], 1.1)} for p in produtos
]
print('Mesmo caso anterio, agora substituindo parte por uma função')
print_iter(novos_produtos)

#agora opção com 'parcial'. Esta opção está usando a mesma função 'aumentar_porcentagem' acima.
aumentar_dez_por_cento = partial(#função que recebe outra função
    aumentar_porcentagem, porcentagem=1.1
)
novos_produtos = [
    {**p, 'preco': aumentar_dez_por_cento(p['preco'])} for p in produtos
]
print("agora opção com 'parcial'")
print_iter(novos_produtos)


#agora usando 'map'
def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco':aumentar_dez_por_cento(
            produto['preco']
        )
    }
novos_produtos = map(#o primeiro parâmetro do 'map' é um função.
    muda_preco_de_produtos, produtos
)
print("agora usando 'map'")
print_iter(novos_produtos)

#exemplo, mais simples de 'map'
exemplo= list(map(#o 'map' foi 'envolvido' por uma list para que não se esgote
    lambda x: x*3,
    [1,2,3,4]
))
print(exemplo)