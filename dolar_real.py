

import requests

resposta = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL'
).json()


valor_compra = float(resposta['USDBRL']['bid'])
valor_venda = float(resposta['USDBRL']['ask'])

print("--"*30)
print(f"Dólar Hoje R$ {valor_compra}".center(50))
print("--"*30)

print(f"Valor de compra: R$ {valor_compra:.4f}")
print(f"Valor de venda: R$ {valor_venda:.4f}")
print("--"*30)

def dolar_real():
    while True:
        try:
            texto = input("🇺🇸 Dólar americano:")
            comprar = float(texto.replace(".","").replace(",","."))
            reais = valor_venda *  comprar
            print(f"Total em (R$) R$: {reais:.2f}")
            break
        except ValueError:
            print("Valor inválido. Ex: 1.500,00")

            




