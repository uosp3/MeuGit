# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy) - copia rasa
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa={
    'nome':'Edson',
    'sobrenome':'Gomes',
    'idade': 62,
    'altura': 1.64,
    'endereços':[
        {'rua': 'Doze', 'número': 561},
        {'av': 'Jequitinhonha', 'número':230},
    ],
}

chave='profissão' #nova chave associada a uma variável
pessoa[chave] = 'aposentado' # cria uma nova chave e valor no dicionario
del pessoa['idade'] #apagar uma chave (e valor)
pessoa.setdefault('idade', 0) # setdefault - adiciona valor se a chave não existe

print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['profissão'])
print('.'*30)

if pessoa.get('idade') is None: #verificando se a chave existe.
    print('Esta chave não existe')
print('/-/'*30)

for chave in pessoa:
    print(chave,':', pessoa[chave])

print('='*30)
print(len(pessoa)) # quantas chaves tem o dicionário
print(list(pessoa.keys())) #retorna uma list das chaves.(pode ser tuplas tb)
print(list(pessoa.values())) #retorna os valores do dicionario
print('.'*30)

print(list(pessoa.items()))
print('+'*30)
for chave, valor in pessoa.items():
    print(chave, valor)

# copy - retorna uma cópia rasa (shallow copy) - copia rasa
people = pessoa #Neste caso as alterações feitas em qualquer um dos dicionários vai afetar o outro.
people = pessoa.copy() #Neste caso as alterações feitas em qualquer um dos dicionários vai afetar o outro.

import copy
people = copy.deepcopy(pessoa) #neste caso o que for feito em um dicionario não afetará o outro (copia profunda.)

print('.'*30)
nome = pessoa.pop('nome')#grava o nome na variável e apaga a chave.
print(nome)
print(pessoa)
print('.'*30)

ultima_chave = pessoa.popitem()#apaga a última chave do dicionario
print(ultima_chave)
print(pessoa)

print('.'*50)
pessoa.update({ #atualiza o dicionario, troca valores ou cria novas chaves.
    'sobrenome': 'Santos',
    'idade': 62
})
pessoa.update(nome='Edson', idade=61) #a atualização tb pode ser feita assim.

print('.'*50)
tupla = (('nome', 'uosp3'), ('idade', 18))#atualiza usando tupla
pessoa.update(tupla)
print(pessoa)

print('.'*50)
lista = [['nome', 'Nosde'], ['idade', 28]]#atualiza usando lista
pessoa.update(lista)
print(pessoa)