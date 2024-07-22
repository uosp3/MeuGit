#x=10
try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo")
finally:
    print("Fim do tratamento")

num="Edson"
if not type(num) is int:
    raise Exception("Somete numeros permitidos")
else:
    print(num)