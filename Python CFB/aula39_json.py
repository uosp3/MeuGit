import json

with open("aula39_json_arquivoExterno.py") as f: #caminho do arquivo
    jogador=json.load(f)

#imprimir chaves
for c in jogador:
    print(c)
print("\n")

#imprimir itens
for i in jogador.items():
    print(i)
print("\n")

#imprimir valores
for v in jogador.values():
    print(v)
print("\n")

#imprimir valor de uma chave específica.
print(jogador["nome"])
print("\n")

#imprimir itens da mochila
for im in jogador["mochila"]:
    print(im)
print("\n")

#imprimir itens das aeronaves
for a in jogador["aeronaves"]:
    print(a)
print("\n")

#imprimir tipos das aeronaves
for a in jogador["aeronaves"]:
    print(a["tipo"])
print("\n")

#imprimir tipos e habilidades das aeronaves
for a in jogador["aeronaves"]:
    print(a["tipo"], "-", a["habilidade"])
print("\n")