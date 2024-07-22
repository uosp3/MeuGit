#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34704388#questions/19560002
lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2), {0, 1}, {'nome':'Edson'},
]

for item in lista:
    print(item, isinstance(item, set)) #verifica qual(is) item da lista é um set

for item in lista:
    if isinstance(item, set):#verifica se é um set
        item.add(5)
        print('Set: ', item)
    
    elif isinstance(item, str):#verifica se é um str
        print('String ', item.upper())

    elif isinstance(item, (int,float)):
        print('Int ou float ', item)

    else:
        print('outro ', item)