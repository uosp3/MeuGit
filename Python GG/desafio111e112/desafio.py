#Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados moeda e dado.
#Transfira todas a funções utilizadas nos desafios 107 a 110 para o primeiro pacote e mantenha tudo funcionando.
import utilidadescev.moeda.moeda as moeda
import utilidadescev.dado.dado as dado


#p=float(input('Digite o preço: R$'))
dindin=dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(dindin, 90, 35)

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