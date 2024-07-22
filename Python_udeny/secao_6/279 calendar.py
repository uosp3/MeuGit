# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35288530#questions
# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

print(calendar.calendar(2024))  # exibe o calendário de 2024
print(calendar.month(2024, 3))  # exibe o mes 3/2024
print('*'*30)

print(calendar.monthrange(2024, 3))
# numero dia primeiro do mes e ultimo dia do mes

print('*'*30)
nome_primeiro_dia_mes, ultimo_dia_mes = calendar.monthrange(2024, 3)
print(list(calendar.day_name))  # dias da semana
print('.'*30)
print(calendar.day_name[nome_primeiro_dia_mes])
print(ultimo_dia_mes)
print('.'*30)

print(calendar.day_name[calendar.weekday(2024, 3, ultimo_dia_mes)])
# nome do último dia do mes

for week in calendar.monthcalendar(2024, 3):
    for day in week:
        if day == 0:
            continue
        print(day, end=' ')
