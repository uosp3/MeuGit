# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
fmt = '%d/%m/%Y'
vr_emprestimo = 1_000_000
vr_parcela = vr_emprestimo/60
formatado = locale.format_string('%.2f', vr_parcela, grouping=True)
data_emprestimo = datetime.strptime('20/12/2020', fmt)
data_final = data_emprestimo + relativedelta(years=5)
diferenca = data_final - data_emprestimo
print(f"Empréstimo de R${vr_emprestimo:.2f} contratado em "
      f"{data_emprestimo.strftime('%d/%m/%Y')}", end=' ')
print(f'por um perído de {int(diferenca.days/30)} meses, tendo com data final '
      f'{data_final.strftime('%d/%m/%Y')}')

conta = 0
for mes in range(30, diferenca.days-1, 30):
    conta += 1
    proxima_parcela = data_emprestimo + relativedelta(months=conta)
    print(f'Parcela {conta:02d}: {
          proxima_parcela.strftime('%d/%m/%Y')} {formatado}')

# O CÓDIGO ABAIXO FOI FEITO PELO PROFESSOR, o código acima foi minha solução
# from datetime import datetime

# from dateutil.relativedelta import relativedelta

# valor_total = 1_000_000
# data_emprestimo = datetime(2020, 12, 20)
# delta_anos = relativedelta(years=5)
# data_final = data_emprestimo + delta_anos

# data_parcelas = []
# data_parcela = data_emprestimo
# while data_parcela < data_final:
#     data_parcelas.append(data_parcela)
#     data_parcela += relativedelta(months=+1)

# numero_parcelas = len(data_parcelas)
# valor_parcela = valor_total / numero_parcelas

# for data in data_parcelas:
#     print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

# print()
# print(
#     f'Você pegou R$ {valor_total:,.2f} para pagar '
#     f'em {delta_anos.years} anos '
#     f'({numero_parcelas} meses) em parcelas de '
#     f'R$ {valor_parcela:,.2f}.'
# )
