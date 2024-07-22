#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34613614#questions/19560002
#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34625964#questions/19560002
lista = ['Edson','Laine','Bianca','Luisa']
nome1, nome2, nome3, nome4 = lista
print(nome2)

nome1, nome2, nome3, nome4 = ['Edson','Laine','Bianca','Luisa']
print(nome3)

nome1, *sobrou= ['Edson','Laine','Bianca','Luisa']#se a quantidade de variáveis não for suficiente o asterisco (*) coloca no que restou na variável precedida do *
print(sobrou)

_, nome2, *_ = ['Edson','Laine','Bianca','Luisa'] # o _ seria para o caso de não precisar dos dados, nesse caso joga-se os dados no anderline.
print(nome2) 

#DESEMPACOTAMENTO
string = 'ABCD'
familia = ['Edson','Laine','Bianca',1,2,3 ,'Luisa']
print(familia) #mosta a lista
print(*familia) #mosta os nomes como se fossem passagem de argumentos
print(*string)

grupos =[
    ['maria','helena'],
    ['elaine'],
    ['luiz','joão','eduarda','edson']
]
print(*grupos, sep='\n')
print(*grupos)