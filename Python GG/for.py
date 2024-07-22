for c in range(0,7,2):#conta de zero até SEIS pulando de 2 em 2
    print(c)

lanche= ("Hamburger","Suco","Pizza","Pudim","Batata Frita")

for cont in range(0,len(lanche)):
    print(lanche[cont])
#as duas linhas abaixo fazem o mesmo que as duas linhas acima.E pode "pegar", se quiser, o índice.
for comida in lanche:
    print(comida)
#no for abaixo pode ser "pegado" o elemento e o índice.
for posicao, comida in enumerate(lanche):
    print(f"comida: {comida} na posição: {posicao}")