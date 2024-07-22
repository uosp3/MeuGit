#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34552984#questions/19560002
a = "AAAAA"
b = "BBBB"
c = 1.1

#as variáveis ficam na mesma ordem
string = 'a={} b={} c={}'
formato = string.format(a, b, c)
print(formato)

#usando ídices não importa a ordem
string = 'b={1} a={0} c={2}'
formato = string.format(a,b,c)
print(formato)

#nomeando com parâmetros
string = 'b={1} c={nome3} a={0}'
formato = string.format(a,b,nome3=c)
#quando um argumento é nomeado com um parâmetro todos os outros após eles obrigatoriamente tem que ser nomeados.
print(formato)
