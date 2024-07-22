#https://www.youtube.com/watch?v=DKUCqkgyvCY&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=37
import json

carros_dictionary={
    "marca": "honda",
    "modelo": "HRV",
    "cor": "preta"
}
#dictionary -> converte para objeto json

carros_list=["honda", "volkswagem", "ford", "chevrolet"]
#list -> converte para array json

carros_tupla=("honda", "volkswagem", "ford", "fiat", "chevrolet")
#tupla -> converte para array json

carros_j=json.dumps(carros_dictionary, indent=4, separators=(": ","="), sort_keys=True) #converte o dictinary para objeto json, faz uma identação de 4 espaços e coloca o sinal de '=' como separador e ordena pela chave.
print(carros_j)