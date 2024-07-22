def titulo(msg):
    print('-'*(len(msg)+15))
    print(f'{msg}'.center(len(msg)+15))
    print('-'*(len(msg)+15))
    return msg

def opcoes(msg):
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-'*(len(msg)+15))
    opcao=input('Sua opção: ')
    while True:
        try:
            n=int(opcao)
            if n>0 and n<4:                            
                break
            else:
                print('Opção inválida, redigite...')
                opcao=input('Sua opção: ')                
        except:
            print('Entrada inválida, redigite')
            opcao=input('Sua opção: ')
    if n==1:
        return 'Pessoas cadastradas'
    if n==2:
        return 'Novo cadastro'
    else:
        return 'Saindo do sistema...Até logo!' 
            

