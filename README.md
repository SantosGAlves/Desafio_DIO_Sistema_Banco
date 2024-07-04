# Banco em Python

Este é um programa simples de simulação de um sistema bancário, escrito em Python, que permite ao usuário realizar operações bancárias básicas como depósito, saque e visualização de extrato.

## Funcionalidades

O programa oferece quatro opções principais:
1. **Depositar**: Permite ao usuário adicionar fundos à sua conta.
2. **Sacar**: Permite ao usuário retirar fundos da sua conta, respeitando um limite diário e um número máximo de saques.
3. **Extrato**: Permite ao usuário visualizar o histórico de transações e o saldo atual da conta.
4. **Sair**: Encerra a execução do programa.

## Código

### Interface do Usuário

A interface do usuário é um menu de texto simples, representado pela variável `hub`. O usuário deve inserir o número correspondente à operação desejada:

```python
hub= '''
-----------------
| [1] Depositar |
|  [2] Sacar    | 
| [3] Extrato   |
|  [4] Sair     |
-----------------
'''
```

### Variáveis Globais

As variáveis globais são usadas para armazenar o estado da conta bancária:

- `saldo`: Armazena o saldo atual da conta.
- `limite`: Define o limite máximo de saque permitido por operação.
- `extrato`: Armazena o histórico de transações.
- `numero_saques`: Contabiliza o número de saques realizados.
- `LIMITE_SAQUES`: Define o número máximo de saques permitidos por dia.

```python
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
```

### Loop Principal

O programa entra em um loop `while` que continua executando até que o usuário escolha a opção de sair (`4`).

### Depósito

Quando o usuário escolhe a opção de depósito (`1`), o programa solicita o valor a ser depositado. Se o valor for positivo, ele é adicionado ao saldo e registrado no extrato.

```python
if opcao == "1":
    valor = float(input('''__________________ Depósito __________________
    \nInforme o valor do depósito:'''))
    print("______________________________________________")
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("\n\Valor inserido é inválido/")
```

### Saque

Quando o usuário escolhe a opção de saque (`2`), o programa verifica se:
- O valor do saque não excede o saldo disponível.
- O valor do saque não excede o limite permitido por operação.
- O número de saques não excede o limite diário.

Se todas as condições forem atendidas, o valor é subtraído do saldo e registrado no extrato.

```python
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
```

### Extrato

Quando o usuário escolhe a opção de extrato (`3`), o programa exibe o histórico de transações e o saldo atual. Se não houver transações, uma mensagem informativa é exibida.

```python
elif opcao == "3":
    print("################### Extrato ###################")
    print("Não houve transações" if not extrato else extrato)
    print(f"\nSaldo = R$ {saldo:.2f}")
    print("###############################################")
```

### Sair

Quando o usuário escolhe a opção de sair (`4`), o loop `while` é interrompido e o programa termina.

```python
elif opcao == "4":
    break
```

### Validação de Entrada

Se o usuário inserir um valor inválido, uma mensagem de erro é exibida.

```python
else:
    print("Valor inválido")
```

## Conclusão

Este programa é uma maneira simples e eficiente de simular operações bancárias básicas. Pode ser estendido para incluir funcionalidades adicionais, como transferência de fundos entre contas ou gerenciamento de contas múltiplas.
