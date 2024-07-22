# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35294620#questions
# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # usa a config de idioma PORT
locale.setlocale(locale.LC_ALL, '')  # usa a config de idioma do SO

print(calendar.calendar(2024))
