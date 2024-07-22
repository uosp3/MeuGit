x=["Carro", "Aviao", "Navio", 1, 58.3, True] #List/Array - o python permite misturar tipos em um array
x[0]="Onibus" #substitui Carro por Onibus no array

print ("Valor: " + x[0])
print("Tipo: "+str(type(x)))

x=("Carro", "Aviao", "Navio", 1, 58.3, True) #Tupla, parece um array mas não permite acrescentar/alterar itens.

print ("Valor: " + x[0])
print("Tipo: "+str(type(x)))

x=range(0,100,1) #Cria um list/array de zero até 100
print ("Valor: " + str(x[0]))
print("Tipo: "+str(type(x)))

x={ #Dictionary
    "canal":"CFB Cursos",
    "curso":"Curso de Python",
    "nome":"Edson"
}
print ("Valor: " + x["nome"])
print("Tipo: "+str(type(x)))

x={5,7,4,5,7,4,8}#set
print ("Valor: " + str(x))#lista os itens exclusivos/sem repetir.
print("Tipo: "+str(type(x)))

x=frozenset([5,7,4,5,7,4,8]) #não permite alterar/acrescentar itens.