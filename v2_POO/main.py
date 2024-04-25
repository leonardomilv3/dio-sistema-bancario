def menu():
    menu = """

    --- Sistema Bancário ---

    Operações disponíveis:
    - 1: operação de depósito
    - 2: operação de saque
    - 3: operação de extrato
    - 4: sair do sistema

    Digite apenas o número da operação desejada: """

    print(menu(), end='')



def main():
    

    while(True):
        menu()

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



main()
