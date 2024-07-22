#https://www.youtube.com/watch?v=P0aW1czXHio
import requests
import time

#criar um decorator calcular_tempo
def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        print('Vou pegar a cotação')
        funcao()
        print('Peguei a cotação do dolar')
        tempo_final = time.time()  
        print(f'Duração foi de {tempo_final-tempo_inicial} segundos')     
    return wrapper

@calcular_tempo
def pegar_cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_cotacao_dolar()