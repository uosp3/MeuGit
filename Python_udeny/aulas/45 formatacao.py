"""
https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34570386#questions/19560002
s - string
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o número a aparecer antes dos zeros ***
sinal - + ou -
ex.: 0>-100,.1f
conversion flags - !r !s !a
"""
variavel = "ABC"
print(f'.{variavel:>10}') #coloca 10 caracteres(a escolher) à esquerda da variável
print(f'{variavel:<10}.') #coloca 10 caracteres(a escolher) à direita da variável
print(f'{variavel:^10}') #coloca a variável centralizada entre 10 caracteres(a escolher)
print(f'{-1000.45934049:+,.2f}')#quantidade de casas decimais(2 no caso) que se deseja no número e a vírgula é o separador de milhar.O sinal de mais(+) faz com que o python mostre se o número é negativo ou positivo.
print(f'{-1000.45934049:0=+10,.2f}')# *** mesmo exemplo preechendo com zeros à esquerda.Neste caso não foi usado o > e sim o =
print(f'O hexadecimal de 1500 é {1500:08X}')