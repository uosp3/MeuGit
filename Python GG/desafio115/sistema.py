from lib.interface import *
from lib.arquivo import *
from time import sleep

arq= 'desafio115/lib/arquivo/cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta==1:
        #listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta ==2:
        #cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade=leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta ==3:
        cabecalho('Saindo do sistema...Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)