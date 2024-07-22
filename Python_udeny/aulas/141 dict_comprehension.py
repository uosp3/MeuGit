#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34693222#questions/19560002
produto = {
    'nome': 'Caneta',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor,str) else valor
    for chave, valor
    in produto.items()
    if chave!='categoria'
}
print(dc)
#o que está à esquerda do FOR é o que comporá o dc
#mas ainda assim tem uma condição que converterá as string para maiúscula
#o que está à direita são as condições para o que comporá o dc
#neste caso, a categoria ficará de fora.