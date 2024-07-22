curso="Curso de Python"

print(curso[0:5]) # python interpreta uma string com uma list/array e, neste caso, imprime os caracteres da posição 0 até 5.
print("Tamanho: "+str(len(curso)))#retorna o tamanho da string

curso=" Curso de Python "
print(curso.strip())#remove espaços antes e depois da string

curso="Curso de Python"
print(curso.lower())#converte para minusculo e tira os espaços.
print(curso.upper())#converte para maiúsculo e tira os espaços.
print(curso.replace("Python","Javascript"))#sustitui dados na string.

a=curso.split(" ")#separa a string em parte usando um espaço(ou outro caractere)
print(a[0])#imprime apenas a parte 0 da list/array gerado pelo split.

texto="Curos de Python"
palavra="python"
res= palavra.upper() in texto.upper() #verifica se a palavra está contida na string
res= palavra.upper() not in texto.upper() #verifica se a palavra não está contida na string

print(res)

cidade="Governador Valadares"
dia=29
mes="Janeiro"
ano=2024
canal="CFB Cursos"
data="{},{} de {} de {}\n\"{}\""#\n quebra a linha e \" coloca entre aspas

print(data.format(cidade,dia,mes,ano,canal))

data = f"{cidade}, {dia} de {mes} de {ano}"#mesmo que o metodo format
print(data)

#pode usar caracteres para 
    #quebra de linha "\n"
    #aspas '\"'
    #tab "\t"
    #backspace "\b" ...