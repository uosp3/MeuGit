#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34785926#questions/19560002
# JSON () "JavaScript Object Notation" (Notação de Objetos JavaScript)
#O QUE É JSON?  https://www.youtube.com/watch?v=XmCrArtfjaQ
import json

pessoa = {
    'nome': 'Edson Gomes 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

#cria o arquivo (aula117.json)
with open('aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False, #codificação para acentos, cedilhas, etc...
        indent=2, #formata para melhor visualizar
    )

#abre o arquivo criado acima.
with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])