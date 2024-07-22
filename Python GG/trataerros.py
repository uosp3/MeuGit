try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r=a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipo de dados que vc digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um númeo por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informa os dados')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__cause__}') #pode ser sem o __xxx__
else: #opcional
    print(f'O resultado é {r:.1f}')
finally: #opcional
    print('Volte sempre! Muito obrigado!')