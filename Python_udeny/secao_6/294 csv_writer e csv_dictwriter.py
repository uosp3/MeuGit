# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35431466#questions/21086260
# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / '294 csv.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

print(lista_clientes[0].keys())  # ver quais as chaves que tem no dict da list

with open(CAMINHO_CSV, 'w', encoding='utf8', newline='') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()  # escreve o cabeçalho.

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)


# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)
