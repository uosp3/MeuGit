dados={}
#ou
dados1=dict()
dados={"nome":"Edson", "idade": 62}
print(dados)
dados["sexo"]="M" #adiciona mais um elemento ao dict
print(dados)
del dados["idade"]#deleta o elemento
print(dados)

filme={"titulo":"Star Wars",
       "ano": 1977,
       "diretor":"George Lucas"
        }
for k,v in filme.items():
    print(f"O {k} é {v}")
for k in filme.keys():
    print(k)
for v in filme.values():
    print(v)

print(filme.values())#mostra os valores
print(filme.keys())#mostra os nomes dos campos
print(filme.items())#mostra tudo

#um dicionário dentro de uma lista
locadora=[{"titulo":"Star Wars",
       "ano": 1977,
       "diretor":"George Lucas"
        },
        {"titulo":"Avengers",
       "ano": 2012,
       "diretor":"Joss Whedon"
        },
        {"titulo":"Matrix",
       "ano": 1999,
       "diretor":"Wachowski"
        }]
print(locadora[0]["ano"])
print(locadora[2]["titulo"])
print(locadora[1]["diretor"])
#*************************************************************
pessoas = {"nome":"Edson", "Sexo":"M", "idade":62}
pessoas["nome"]="Gomes" #substitui o nome.
pessoas["peso"]=70 #adiciona um elemento ao dicionário.
print(f"O {pessoas["nome"]} tem {pessoas['idade']} anos e pesa {pessoas['peso']} kg")
#***************************************************************
brasil=[]
estado1={"uf":"Rio de Janeiro", "sigla":"RJ"}
estado2={"uf":"Minas Gerais", "sigla":"MG"}
estado3={"uf":"São Paulo", "sigla":"SP"}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
print(brasil)
print(brasil[1]["uf"])
#***************************************************************
estado={}
brasil=[]
for c in range(0,3):
    estado["uf"]=str(input("Unidade Federativa: "))
    estado["sigla"]=str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    print(e)
