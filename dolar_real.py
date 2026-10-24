



def dolar_real(valor_venda):
    print("--"*30)
   
    print(f"Valor de venda: R$ {valor_venda:.4f}")
    while True:
        try:
            texto = input("🇺🇸 Dólar americano:")
            comprar = float(texto.replace(".","").replace(",","."))
            reais = valor_venda *  comprar
            print(f"Total em (R$) R$: {reais:.2f}")
            break
        except ValueError:
            print("Valor inválido. Ex: 1.500,00")

            




