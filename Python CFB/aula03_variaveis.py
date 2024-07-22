#variável se declarada fora de um escopo é global mas dentro de um bloco/escopo pode-se declarar uma variável como global desde que isto fique explicitado.

#a variável abaixo é global
canal="CFB Cursos"

def cn():
    #a variável abaixo foi explicitada como global.Para que esta variável seja acessada fora do escopo é necessário que a função seja chamada.
    global canal2
    canal2="Teste"

cn()
print(canal2)
print(canal)
