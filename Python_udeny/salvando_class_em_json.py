#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34860736#questions
# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

caminho_arquivo = 'salvando_classe_em_json.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Edson', 62)
p2 = Pessoa('Laine', 56)
p3 = Pessoa('Luisa', 26)
p4 = Pessoa('Bianca', 33)

dados = [vars(p1),p2.__dict__,vars(p3),vars(p4)] 
#vars() ou .__dict__ converte os dados para um dict
print(dados)

def fazer_dump():
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        print("Fazendo dump")
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

#como um arquivo depende do outra o if abaixo faz com que a função 'fazer_dump' so seja executada a partir desse arquivo.Vide outro arquivo de mesmo nome que este com 'b' no final do nome.
if __name__ == '__main__':
    print("Ele é o __main__")
    fazer_dump()