saldo = 0
while True:
    opcao = input("\n1. Depósito. \n2. Saque. \n3. Extrato. \n4. Sair\nEscolha uma opção: ")
    if opcao == '1':
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f'Depósito de R${valor_deposito:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')
    elif opcao == '2':
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque <= saldo:
            print(f"Saque no valor de R${valor_saque:.2f} foi realizado com sucesso.")
        else:
            print("Erro!! Saldo insuficeiente!!")
    elif opcao == '3':
        print(f'\nExtrato bancário:')
        print(f'Saldo atual: R${saldo:.2f}')
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
