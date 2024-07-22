#Closure e funções que retornam outras funções
#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34659136#questions
def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar #aqui foi omitido os () que faria o fechamento da função. Eles aparecem no print ao lado da variável.

s1=criar_saudacao('Bom dia', 'Edson')
s2=criar_saudacao('Boa noite', 'Gomes')

print(s1())
print(s2())
