carros=[
    ["Modelo","HRV"],
    ["Fabricante","Honda"],
    ["Ano", "2016"]
]

print(carros[2][0])

carros.append(["cor","Prata"])#acrescentar dados à matriz

carros[2][1]=2024

for l,c in carros:
    print("Linha: ",l," | Coluna: ", c)