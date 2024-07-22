#https://www.youtube.com/watch?v=ItjusOlIzqc&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=38
import json

# {
#     "nome":"Edson",
#     "time":"aviadores",
#     "vivo":"True",
#     "energia":100,
#     "mochila":["pederneira","corda","linha","arame"],
#     "aeronaves":[
#         {"tipo":"transporte","habilidade":80},
#         {"tipo":"ataque","habilidade":100},
#         {"tipo":"reconhecimento","habilidade":50}
#     ]
# }
# a estrutura acima é a mesma abaixo, visto como json. Neste caso tem que estar tudo na mesma linha.

jogador_j='{"nome":"Edson", "time":"aviadores","vivo":"True","energia":100,"mochila":["pederneira","corda","linha","arame"],"aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhecimento","habilidade":50}]}'
#dictionary -> converte para objeto json

jogador=json.loads(jogador_j)

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