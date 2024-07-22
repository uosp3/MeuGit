l_carros=["HRV","Golf","Argo"]#list/array
t_carros=("HRV","Golf","Argo")#tupla

#tupla não aceitam alterações...

#truque para alterar, criar uma list igual a tupla
l_carros=list(t_carros)
#fazer na list a alteração desejada
l_carros[2]="Focus"
#refazer a tupla a partir da list
t_carros=tuple(l_carros)

for x in t_carros:
    print(x)