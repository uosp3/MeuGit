class Carro:
    velMax=0
    ligado=False
    cor=""

c1=Carro()
c2=Carro()
c3=Carro()

c1.velMax=200
c1.cor="Preto"
c1.ligado=False

print("Velocidade Maxima: ",c1.velMax)
print("Cor: ",c1.cor)
estado="S" if c1.ligado else "N"
print("Ligado: ",estado)