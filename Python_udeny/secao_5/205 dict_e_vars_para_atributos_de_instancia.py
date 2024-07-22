# __dict__ e vars para atributos de instância
#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34860616#questions
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35} 
p1 = Pessoa(**dados) # uma forma de passar o dict acima para a classe.
# p1.nome = 'EITA'
# print(p1.idade)
# p1.__dict__['outra'] = 'coisa' #usado para criar um novo atributo da classe. Isse não é comum de acontecer. Apenas informativo.
# p1.__dict__['nome'] = 'EITA' # altera a chave 'nome'. Conforme comentário acima isso não é comum na programação.
# del p1.__dict__['nome'] # apaga a chave(atributo) 'nome'. Conforme comentários anteriores isso não é de praxe ser feito com __dict__
# print(p1.__dict__) # gera um dict dos atributos da classe.
# print(vars(p1))    # gera um dict dos atributos da classe.
# print(p1.outra)
# print(p1.nome)
print(vars(p1))
print(p1.nome)