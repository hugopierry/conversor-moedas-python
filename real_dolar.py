

def real_dolar(valor_venda):
    while True:
        try:
            texto = input("🇧🇷 Real brasileiro: ")
            comprar = float(texto.replace(".","").replace(",","."))
            conversao = (comprar / valor_venda)
            print(f"US${conversao:.2f}")
            break
        except ValueError:
            print("Valor inválido. Ex: 1.500,00")

            


