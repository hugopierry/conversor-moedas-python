from dolar_real import dolar_real
from real_dolar import real_dolar
from buscar_cotacao import buscar_cotacao


def menu():
    compra, venda = buscar_cotacao()

    while True:
        print("=" * 60)
        print("💱 CONVERSOR DE MOEDAS".center(60))
        
        if compra is None:
            print("Cotação indisponível".center(60))
        else: 
            print(f"\nCompra: R$ {compra:.4f} | Venda: R$ {venda:.4f}".center(60))
        
       
        
        print("=" * 60)

        print("  [1] 🇺🇸 Dólar → 🇧🇷 Real")
        print("  [2] 🇧🇷 Real → 🇺🇸 Dólar")
        print("  [0] 🚪 Sair")
        print("=" * 60)
        opcao = input("Escolha uma opção: ").strip()
        print("=" * 60)

        if opcao == "1":
            if venda is not None:
                dolar_real(venda)
            else:
                print("Conversão indisponível: cotação não encontrada.")
        elif opcao == "2":
            if venda is not None:
                real_dolar(venda)
            else:
                print("Conversão indisponível: cotação não encontrada.")
        elif opcao == "0":
            print("\nSaindo do sistema...")
            print("\nAté logo!")
            break
        else:
            print(f"\nOpção '{opcao}' inválida!")
            print("Opções válidas: 1, 2, ou 0.")

if __name__ == "__main__":
    try:
        menu()
    except Exception as erro:
        print(f"\n❌ Erro inesperdo: {erro}")
    input("\n\nPressione ENTER para sair do programa.")


