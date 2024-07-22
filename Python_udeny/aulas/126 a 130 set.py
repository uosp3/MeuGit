# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34688658#questions/19560002
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34688900#questions/19560002
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34689024#questions/19560002
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34689148#questions/19560002
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34689638#questions/19560002
# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard
s1.add(5) #adiciona
s1.update('olá mundo') # atualiza adicionando
s1.update(('olá mundo',)) # atualiza adicionando
print(s1)
s1.discard('Luiz')#apaga um dado
print(s1)
s1.clear() #Limpa

# Operadores úteis:
# união | união (union) - Une
s1={1,2,3}
s2={2,3,4}
s3=s1 | s2
print(s3)
# intersecção & (intersection) - Itens presentes em ambos
s3=s1 & s2
print(s3)
# diferença - Itens presentes apenas no set da esquerda
s3=s1 - s2
print(s3)
# diferença simétrica ^ - Itens que não estão em ambos
s3=s1 ^ s2
print(s3)