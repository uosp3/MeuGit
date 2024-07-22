# dir, hasattr e getattr em Python
#saber quais métodos estão disponíveis na string
#no debug, colocando um ponto de interrupção(nas opções do terminal), digita a string ou dir(string) para visualizar os métodos.
#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34705160#questions
string = 'Edson'
metodo = 'upper'

if hasattr(string, metodo):#checa se o objeto tem o nome(método?)
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)