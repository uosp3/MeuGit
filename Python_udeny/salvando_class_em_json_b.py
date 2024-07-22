#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34860736#questions
# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

from salvando_class_em_json import caminho_arquivo, Pessoa, fazer_dump

with open(caminho_arquivo, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    p4 = Pessoa(**pessoas[3])

    print(p1.nome, p1.idade)