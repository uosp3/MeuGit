# Problema dos parâmetros mutáveis em funções Python
# Não use parâmetros mutáveis em valor padrão de funções, caso contrário cada vez que a função for executada o python usará a mesma lista.
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)