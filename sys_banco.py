saldo = 0
#número de saques diários
saque_diario = 0
#limte do valor do saque
LIMITE_SAQUE = 500
#limite de saques diários
max_saque_diario = 3

def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print(f'Depósito de R${valor:.2f} realizado.')
    else:
        print('Valor inválido!')

def saque(valor):
    global saldo, saque_diario
    # Verifica se o valor do saque é válido e respeita o limite de R$500
    if valor <= 0:
        print('Digite um valor maior que R$0 para efetuar o saque.')
        return
    
    if valor > LIMITE_SAQUE:
        print('O limite para saques é de R$500,00.')
        return
    
    if valor > saldo:
        print('Saldo insuficiente.')
        return
    
    if saque_diario >= max_saque_diario:
        print('Limite de saque diário atingido.')
        return 
    
    # Após passar em todas as verificações, realiza o saque
    saldo -= valor
    saque_diario += 1
    print(f'Saque de R${valor:.2f} efetuado.')

def extrato():
    print(f"\nExtrato bancário:")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Saques realizados hoje: {saque_diario}/{max_saque_diario}")

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Sair")
        
        opcao = input("Digite a opção: ")
        
        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$ "))
            deposito(valor)
        
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$ "))
            saque(valor)
        
        elif opcao == "3":
            extrato()
        
        elif opcao == "4":
            print("Saindo do sistema bancário.")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Chama o menu
menu()
