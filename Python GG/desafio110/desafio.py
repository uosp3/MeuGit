#https://www.youtube.com/watch?v=1Ks218WINT8 vídeo da aula, não está na playlist
#Adicione ao móduto moeda.py criado nos desafios anteriores, um função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que ja temos no módulo criado até aqui
import moeda

p=float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)

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