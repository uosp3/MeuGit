#Chave/key - Valor/Value
carro={
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2016", 
    "Cor":"Prata"
}

carro["Cambio"]= "Automatico" #acrescentar itens

fab=carro["Fabricante"] # ou 
fab2=carro.get("Fabricante")
print(fab)
print(fab2)

#para trocar dados
carro["Cor"]="Preto"
print(carro)

for x in carro:
    print("Chave: ",x) #imprime so chave
    print("Valor: ",carro[x]) #imprime valor

print('\n')

for c,v in carro.items():#dessa forma imprime chave e valor juntos.
    print(c, ": ",v)

if "Modelo" in carro:
    print("Sim, modelo e uma chave \n")

print("Tamanho do Dictionary: ", len(carro))

carro.pop("Cambio") #excluir um item
# tb pode ser com del carro["Cambio"]
carro.clear() #limpa tudo.

print(carro)

###### Dictionary do dictionary #######

carros={
    "Carro1":{
        "Fabricante":"Honda",
        "Modelo":"Civic"
    },
    "Carro2":{
        "Fabricante":"Volkswagem",
        "Modelo":"Golf"
    },
    "Carro3":{
        "Fabricante":"Ford",
        "Modelo":"Focus"
    },
}

print("1.....................................................")
print(carros)
print("2.....................................................")
print(carros["Carro1"])
print(carros["Carro1"]["Fabricante"])

################### Mais opções ###############################

Carro1={
        "Fabricante":"Honda",
        "Modelo":"Civic"
    }
Carro2={
        "Fabricante":"Volkswagem",
        "Modelo":"Golf"
    }
Carro3={
        "Fabricante":"Ford",
        "Modelo":"Focus"
    }

Carros={
    "C1":Carro1,
    "C2":Carro2,
    "C3":Carro3,
}

print("3.......................................................")
print(Carros["C1"])
print(Carros["C1"]["Modelo"])