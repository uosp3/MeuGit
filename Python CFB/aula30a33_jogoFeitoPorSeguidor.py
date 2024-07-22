from random import randint
from time import sleep
lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
listadeJogadas = []
vitoria = False
xOuO = f'{"X":^5}'


def tela():
    print('=' * 30)
    print(f'{"JOGO DA VELHA":^30}')
    print('=' * 30)
    for l in range(0, 3):
        for c in range(0, 3):
            if c < 2:
                print(f'{lista[l][c]:^5}|', end='')
            else:
                print(f'{lista[l][c]:^5}', end='')
        print()
        if l < 2:
            print('-' * 18)


def jogadorJoga():
    global xOuO
    global lista
    global listadeJogadas
    ok = False
    while True:
        n = int(input(f'Vez do jogador, Digite um numero para posição {xOuO}: '))
        if n not in listadeJogadas:
            if 0 < n < 10:
                listadeJogadas.append(n)
                ok = True
                break
            else:
                print('Jogada invalida. ')
    if ok:
        for l in range(0, 3):
            for c in range(0, 3):
                if lista[l][c] == n:
                    lista[l][c] = f'\033[31m{xOuO}\033[m'
                    xOuO = f'{"O":^5}'


def computadorJoga():
    global xOuO
    global lista
    global listadeJogadas
    global pergunta
    ok = False
    while True:
        if len(listadeJogadas) == 9:
            break
        n = randint(1, 9)
        if n not in listadeJogadas:
            if 0 < n < 10:
                listadeJogadas.append(n)
                ok = True
                break
            else:
                print('Jogada invalida. ')
    if ok:
        for l in range(0, 3):
            for c in range(0, 3):
                if lista[l][c] == n:
                    lista[l][c] = f'\033[36m{xOuO}\033[m'
                    if pergunta == 2:
                        xOuO = f'{"O":^5}'
                    else:
                        xOuO = f'{"X":^5}'


def verificarVitoria():
    global vitoria
    # Horizontal
    if lista[0][0] == lista[0][1] and lista[0][1] == lista[0][2]:
        vitoria = True
    if lista[1][0] == lista[1][1] and lista[1][1] == lista[1][2]:
        vitoria = True
    if lista[2][0] == lista[2][1] and lista[2][1] == lista[2][2]:
        vitoria = True
    # Diagonal
    if lista[0][0] == lista[1][1] and lista[1][1] == lista[2][2]:
        vitoria = True
    if lista[0][2] == lista[1][1] and lista[1][1] == lista[2][0]:
        vitoria = True

    # Vertical
    if lista[0][0] == lista[1][0] and lista[1][0] == lista[2][0]:
        vitoria = True
    if lista[0][1] == lista[1][1] and lista[1][1] == lista[2][1]:
        vitoria = True
    if lista[0][2] == lista[1][2] and lista[1][2] == lista[2][2]:
        vitoria = True


maxJogadas = 0
pergunta = int(input('Quem começa primeiro? (Você = 1 / Computador = 2): '))

if pergunta == 1:
    while maxJogadas < 9:
        print('VOCÊ INICIA!')
        tela()
        jogadorJoga()
        tela()
        verificarVitoria()
        maxJogadas += 1
        if vitoria:
            print('Jogador Ganhou!')
            break
        print(f'Computador esta penssando em qual posição vai jogar {xOuO}...')
        sleep(2)
        computadorJoga()
        tela()
        verificarVitoria()
        maxJogadas += 1
        if vitoria:
            print('Computador Ganhou!')
            break

    if maxJogadas == 10:
        print('Deu velha!!!, NIGUEM GANHOU.')
else:
    print('COMPUTADOR INICIA!')
    while maxJogadas < 9:
        tela()
        print(f'Computador esta penssando em qual posição vai jogar {xOuO}...')
        sleep(2)
        computadorJoga()
        tela()
        maxJogadas += 1
        verificarVitoria()
        if vitoria:
            print('Computador Ganhou!')
            break

        jogadorJoga()
        tela()
        verificarVitoria()
        if vitoria:
            print('Jogador Ganhou!')
            break

    if maxJogadas == 10:
        print('Deu velha!!!, NIGUEM GANHOU.')

