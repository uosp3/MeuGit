# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34705092#questions/19560002
# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = [] #false
dicionario = {}#false
conjunto = set()#false
tupla = ()#false
string = ''#false
inteito = 0#false
flutuante = 0.0#false
nada = None#false
falso = False#false
intervalo = range(0)#false


def falsy(valor):
    return 'falsy'if not valor else 'truthy'


print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteito=}', falsy(inteito))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))