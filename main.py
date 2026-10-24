from dolar_real import dolar_real
from real_dolar import real_dolar
from buscar_cotacao import buscar_cotacao




def menu():
    while True:
        print("=" * 60)
        print("💱 CONVERSOR DE MOEDAS".center(60))
        compra, venda = buscar_cotacao()
        if compra is None:
            print("Cotação indisponível".center(60))
        else: 
            print(f"Compra: R$ {compra:.4f} | Venda: R$ {venda:.4f}".center(60))
        
       
        
        print("=" * 60)

        print("  [1] 🇺🇸 Dólar → 🇧🇷 Real")
        print("  [2] 🇧🇷 Real → 🇺🇸 Dólar")
        print("  [0] 🚪 Sair")
        print("=" * 60)
        opcao = input("Escolha uma opção: ").strip()
        print("=" * 60)

        if opcao == "1":
            dolar_real()
        elif opcao == "2":
            real_dolar()
        elif opcao == "0":
            print("\nSaindo do sistema...")
            print("Até logo!")
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


