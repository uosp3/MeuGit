# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34691284#questions/19560002
# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)
print('='*30)

for chave, valor in pessoa.items():
     print(chave, valor)
print('='*30)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}
#juntando dos dicionários em um terceiro
pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)

# args e kwargs
# *args (argumentos não nomeados)
# **kwargs - keyword arguments (argumentos nomeados)
print('/*'*30)
def mostro_argumentos_nomeados(*args, **kwargs):#sempre um * para args e dois ** para kwargs
    print('NÃO NOMEADOS:', args)
    print('*'*30)  
    print('NOMEADOS:')  
    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(1,2, nome='Joana', qlq=123)
print('=*'*30)
mostro_argumentos_nomeados(**pessoas_completa)
print('=*'*30)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)