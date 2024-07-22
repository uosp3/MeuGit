# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35411304#questions/21564524
# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = '290 arquivo_gerado.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(  # caminho absoluto
    os.path.join(
        os.path.dirname(__file__),  # pega o caminho absoluto do arquivo
        NOME_ARQUIVO
    )
)

filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)
