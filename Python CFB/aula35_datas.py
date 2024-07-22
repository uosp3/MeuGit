import datetime

data=datetime.datetime.now() #data atual e horas
nasc=datetime.datetime(1961,10,23)

print(data.day,"/",data.month,"/",data.year)
print(nasc.strftime("%A")) #dia da semana
#%A - texto dia da semana
#%a - texto dia da semana reduzido
#%w - numero do dia da semana
#%d - numero dia do mes
#%b - texto mes reduzido
#%B - texto mes
#%m - numero do mes
#%y - ano com dois digitos
#%Y - ano com 4 digitos
#%H - hora de 00 a 23
#%I - hora de 00 a 12
#%p - AM/PM
#%M - Minutos
#%S - Segundos
#%f - lilisegundos
#%j - dia do ano 001 a 365
#%W - Numero da semana do ano
