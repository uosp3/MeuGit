# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35046686#questions
# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo # faz um generator
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('aula242.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)