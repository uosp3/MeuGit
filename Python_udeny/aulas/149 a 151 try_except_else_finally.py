# try, except, else e finally
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34708520#questions/19560002
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34708926#questions
try:
    print('ABRIR ARQUIVO')
    #8/1
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally: #sempre será executado.
    print('FECHAR ARQUIVO')