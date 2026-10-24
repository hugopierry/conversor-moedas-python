import requests

def buscar_cotacao():
    try: 
        resposta = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL',timeout=5).json()
        compra = float(resposta['USDBRL']['bid'])
        venda = float(resposta['USDBRL']['ask'])
        return compra, venda 
    except (requests.exceptions.RequestException,KeyError, ValueError):
        print("⚠️ Não foi possível buscar a cotação.")
        return None, None
