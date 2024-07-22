# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35817500#questions

# Para ativar o servidor ====> python -m http.server
# é necessári estar na pasta que se deseja abrir o arquivo.

# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443
url = 'http://localhost:8000/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)
