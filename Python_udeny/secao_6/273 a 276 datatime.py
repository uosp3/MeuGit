# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/15273910#questions
# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# Timestamp - segundos contados a partir de 01/01/1970
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from pytz import timezone

data_str_data = '2022/04/20 07:49:23'
data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'

data1 = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)
print(data1)

#
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/15456516#questions
data = datetime.now(timezone('Asia/Tokyo'))
data_agora = datetime.now()
print(f'Data agora {data_agora}')
print(data)  # data atual
print(f'timestamp agora {data.timestamp()}')  # Isso está na base de dados
print(datetime.fromtimestamp(1670849077))

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)

#
#
#
#
#
print('='*30)
# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35266888#questions
# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

# pip install python-dateutil types-python-dateutil
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
delta2 = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inicio)
print(f'delta.days {delta.days}, {delta.years}')
# print(data_fim - delta)
# print(data_fim)
print(f'Relativedelta {data_fim + relativedelta(years=5)}')

delta3 = data_fim - data_inicio
print(delta)
print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)
