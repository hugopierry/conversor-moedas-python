

# 1. Requisição à API
import requests

resposta = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL'
).json()

# 2. Extração dos valores
valor_compra = float(resposta['USDBRL']['bid'])
valor_venda = float(resposta['USDBRL']['ask'])

# 3. Exibição dos resultados
print("--"*30)
print(f"Dólar Hoje R$ {valor_compra}".center(50))
print("--"*30)

print(f"Valor de compra: R$ {valor_compra:.4f}")
print(f"Valor de venda: R$ {valor_venda:.4f}")
print("--"*30)

# Descrição de saída:
 
# bid: cotação de compra informada pela API.
# ask: cotação de venda informada pela API.
# float(): converte o valor recebido em texto para um número decimal.

def real_dolar():
    while True:
        try:
            texto = input("🇧🇷 Real brasileiro: ")
            comprar = float(texto.replace(".","").replace(",","."))
            conversao = (comprar / valor_venda)
            print(f"US${conversao:.2f}")
            break
        except ValueError:
            print("Valor inválido. Ex: 1.500,00")

            


