import json

carros_json='{"marca":"honda", "modelo":"HRV", "cor":"prata"}'
#manipula-se como um dictinary, o dictionary não tem os apostrofos.Vide linha 23
carros=json.loads(carros_json) #converte para dictionary

print(carros)
print(carros["marca"])
print("\n")

for x in carros:
    print(x)#imprime as chaves

print("\n")
for x in carros.values():
    print(x)#imprime os valores

print("\n")
for k,v in carros.items():
    print(k,v)#imprime chaves e valores.


carros_dictionary={"marca":"honda", "modelo":"HRV", "cor":"prata"}
carros_json=json.dumps(carros_dictionary) #converte para json
print(carros_json)