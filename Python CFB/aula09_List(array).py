carros=["HRV","Golf","Argo","Focus"]
carros.append("Civic")#acrescenta itens à lista
carros.append("Fusca")
carros.remove("Argo")#remove um item da lista

print(str(len(carros))+ " Carros na lista")
print(carros)

carros.pop()#remove o último item da lista
print(carros)

del carros[2]#remove o item 2 da lista
print(carros)

carros2=["Chevette", "Uno", "Brasilia", "Celta"]

carros3=list(carros)#copia uma lista para outra

carros4=carros+carros2 #junta duas listas

carros.clear()#limpa a lista
print(carros, " Carros")
print(carros2, " Carros2")
print(carros3, " Carros3")
print(carros4, " Carros 4")