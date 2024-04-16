def deposito():
    global saldo, extratos

    print("\n--- Funcionalidade de Depósito ---\n")

    deposito = float(input("Informe um valor positivo a ser depositado: "))
    
    if deposito > 0:
        saldo += deposito
        deposito_str = '{:.2f}'.format(deposito) 
        extratos.append(f"- Depósito de R$ {deposito_str}\n")
        print("Depósito realizado com sucesso!")
    else:
        print("Erro! Não foi possível realizar o depósito.\n")


def saque():
    global saldo, extratos

    print("\n--- Funcionalidade de Saque ---\n")

    saque = float(input("Informe um valor positivo a ser sacado: "))

    if saque > 0 and saque <= LIMITE_SAQUE and saldo >= saque :
        saldo -= saque
        saque_str = '{:.2f}'.format(saque) 
        extratos.append(f"- Saque de R$ {saque_str}\n")
        print("Saque realizado com sucesso!\n")
    else:
        print("Erro! Não foi possível realizar o saque.\n")


def extrato():
    pass


menu = """

--- Sistema Bancário ---

Operações disponíveis:
- 1: operação de depósito
- 2: operação de saque
- 3: operação de extrato
- 4: sair do sistema

Digite apenas o número da operação desejada: """

LIMITE_DIARIO = 3
LIMITE_SAQUE = float(500)

saldo = float(0)
contador_saque = 0
extratos = []

while(True):
    print(menu, end='')
    opcao = int(input())

    if ( opcao == 1):
        deposito()
    elif ( opcao == 2 ):  
        if contador_saque > 3:
            print("O limite diária de {LIMITE_DIARIO} saques foi atingido!")
        else:
            contador_saque +=1
            saque()
    elif ( opcao == 3 ):
        print(extrato())
    elif ( opcao == 4 ):
        break
    else:
        print("Opção inválida")

        

