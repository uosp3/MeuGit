def aumentar(preco=0, taxa=0, formata=False):
    res = preco+preco*taxa/100
    return res if formata == False else moeda(res)

def diminuir(preco=0, taxa=0, formata=False):
     res = preco-preco*taxa/100
     return res if formata == False else moeda(res)

def dobro(preco=0, formata=False):
     res = preco*2
     return res if formata == False else moeda(res)

def metade(preco=0, formata=False):
     res = preco/2     
     return res if formata == False else moeda(res)

def moeda(preco=0, moeda='R$'):
     res=f'{moeda}{preco:>.2f}'.replace('.',',')
     return res

def resumo(preco=0, aumento=0, reducao=0):
     res=moeda(preco)
     print(f'~'*30)
     print('Resumo do valor'.center(30))
     print(f'~'*30)
     print(f'Preço analisado: \t{moeda(preco)}')
     print(f'O dobro do preço: \t{dobro(preco, True)}')
     print(f'A metade do preço: \t{metade(preco, True)}')
     print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
     print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')
     print(f'~'*30)

#Resultado:
    #~~~~~~~~~~~~~~~~~~
    # Resumo do valor
    #~~~~~~~~~~~~~~~~~~
    #Preço analisado:   R$...
    #Dobro do preço:    R$...
    #Metado do preço:   R$...
    #80% de aumento:    R$...
    #35% de redução:    R$...
    #-------------------------