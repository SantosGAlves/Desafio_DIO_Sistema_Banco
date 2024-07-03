hub= '''
-----------------
| [1] Depositar |
|  [2] Sacar    | 
| [3] Extrato   |
|  [4] Sair     |
-----------------
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(hub)

    if opcao == "1":
        
        valor = float(input('''__________________ Depósito __________________
       \nInforme o valor do depósito:'''))
        print("______________________________________________")
        

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("\n\Valor inserido é inválido/")

    elif opcao == "2":
        valor = float(input('''__________________ Saque __________________
        \nInforme o valor que deseja sacar:'''))
        print("______________________________________________")

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação Inválida, você não possui saldo")

        elif excedeu_limite:
            print("\nOperação Inválida, você não pode sacar além do limite de R$ 500,00")

        elif excedeu_saques:
            print("\nO número máximo que você pode sacar é 3 vezes")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("\n\Valor inválido/")

    elif opcao == "3":
        print("################### Extrato ###################")
        print("Não houve transações" if not extrato else extrato)
        print(f"\nSaldo = R$ {saldo:.2f}")
        print("###############################################")

    elif opcao == "4":
        break

    else:
        print("Valor inválido")

        
