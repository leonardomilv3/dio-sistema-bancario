from classes import *


def verificar_conta(pessoa: PessoaFisica):

    num_conta = int(input("\nInforme o numero da conta: "))

    conta_corrente = None

    for conta in pessoa.contas:
        if num_conta == conta.numero:
            conta_corrente = conta
            break

    if conta_corrente is not None:
        return conta_corrente, True
    
    return 0, False


def depositar(pessoa: PessoaFisica):
    
    conta_corrente, conta_existe = verificar_conta(pessoa)

    if conta_existe:
        valor = float(input("Informe o valor a ser depositado: "))
        transacao = Deposito(valor)
        pessoa.realizar_transacao(conta_corrente, transacao)
    else:
        print("Operação falhou! O numero da conta não existe\n")

    
def sacar(pessoa: PessoaFisica):
    conta_corrente, conta_existe = verificar_conta(pessoa)

    if conta_existe:
        valor = float(input("Informe o valor a ser sacado: "))
        transacao = Saque(valor)
        pessoa.realizar_transacao(conta_corrente, transacao)
    else:
        print("Operação falhou! O numero da conta não existe\n")

def extrato(pessoa: PessoaFisica):
    conta_corrente, conta_existe = verificar_conta(pessoa)

    if conta_existe:
        for transacao in conta_corrente.historico.transacoes[::-1]:
            for k, v in transacao.items():
                print(f"{k}: {v}")
    else:
        print("Operação falhou! O numero da conta não existe\n")


def criar_nova_conta(pessoa: PessoaFisica):
    
    print("\n--- Cadastro de Conta ---\n")
    numero = len(pessoa.contas) + 1

    nova_conta = ContaCorrente(numero, pessoa)
    pessoa.adicionar_conta(nova_conta)

    print("Conta Corrente criada com sucesso!\n")


def listar_contas(pessoa: PessoaFisica):
    for conta in pessoa.contas:
        print(f"\n--- Conta {conta.numero} --- \n")
        print(f"- Saldo da conta: R$ {conta.saldo:.2f}")
        print(f"- Número da conta: {conta.numero}")
        print(f"- Número da agencia: {conta.agencia}")


def criar_novo_usuario() -> PessoaFisica:
    
    print("\n--- Cadastro de Pessoa Física ---\n")
    cpf = str(input("Informe o CPF: "))
    nome = str(input("Informe o nome: "))
    dt_nascimento = str(input("Informe a data de nascimento: "))
    endereco = str(input("Informe o endereço completo: "))

    pessoa_fisica = PessoaFisica(cpf, nome, dt_nascimento, endereco)

    print(f"\nOperação sucedida! Usuário {pessoa_fisica.nome} criado com sucesso!\n")
    return pessoa_fisica


def menu() -> int:
    menu = """\n
    --- Sistema Bancário ---

    Operações disponíveis:\n
    - [1] Operação de depósito
    - [2] Operação de saque
    - [3] Operação de extrato
    - [4] Nova Conta
    - [5] Listar Contas
    - [6] Novo usuário 
    - [7] Sair do sistema

    Digite o número da operação desejada: """

    print(menu, end='')
    opcao = int(input())

    return opcao


def existe_pessoa_fisica(pessoas: list, cpf: str):
    
    encontrei = len(
        [
            cpf for pessoa in pessoas if pessoa.cpf == cpf
        ]
    ) > 0

    if encontrei:
        return True
    
    return False


def consultar_pessoa_fisica(pessoas_fisicas, cpf):
    
    pessoa_fisica = None

    for pessoa in pessoas_fisicas:
        if pessoa.cpf == cpf:
            pessoa_fisica = pessoa
            break

    return pessoa_fisica


def main():
    
    pessoas_fisicas = []

    while(True):
        
        opcao = menu()

        operacao_deposito = opcao == 1 
        operacao_sacar = opcao == 2
        operacao_extrato = opcao == 3
        nova_conta = opcao == 4
        listar_contas_op = opcao == 5
        novo_usuario = opcao == 6
        sair = opcao == 7

        if operacao_deposito:
        
            nenhum_usuario = len(pessoas_fisicas) == 0
            if nenhum_usuario:
                print("Operação falhou! Cadastre uma Pessoa Física primeiro!\n")
            else:
                cpf = str(input("Informe o CPF: "))
                if existe_pessoa_fisica(pessoas_fisicas, cpf):
                    pessoa_fisica = consultar_pessoa_fisica(pessoas_fisicas, cpf)
                    depositar(pessoa_fisica)
                else:
                    print("Operação falhou! O CPF não foi encontrado.")

        elif operacao_sacar:  

            nenhum_usuario = len(pessoas_fisicas) == 0
            if nenhum_usuario:
                print("Operação falhou! Cadastre uma Pessoa Física primeiro!\n")
            else:
                cpf = str(input("Informe o CPF: "))
                if existe_pessoa_fisica(pessoas_fisicas, cpf):
                    pessoa_fisica = consultar_pessoa_fisica(pessoas_fisicas, cpf)
                    sacar(pessoa_fisica)
                else:
                    print("Operação falhou! O CPF não foi encontrado.")

        elif operacao_extrato:

            nenhum_usuario = len(pessoas_fisicas) == 0
            if nenhum_usuario:
                print("Operação falhou! Cadastre uma Pessoa Física primeiro!\n")
            else:
                cpf = str(input("Informe o CPF: "))
                if existe_pessoa_fisica(pessoas_fisicas, cpf):
                    pessoa_fisica = consultar_pessoa_fisica(pessoas_fisicas, cpf)
                    extrato(pessoa_fisica)
                else:
                    print("Operação falhou! O CPF não foi encontrado.")

        elif nova_conta:

            nenhum_usuario = len(pessoas_fisicas) == 0
            if nenhum_usuario:
                print("Operação falhou! Cadastre uma Pessoa Física primeiro!\n")
            else:
                cpf = str(input("Informe o CPF: "))
                if existe_pessoa_fisica(pessoas_fisicas, cpf):
                    pessoa_fisica = consultar_pessoa_fisica(pessoas_fisicas, cpf)
                    criar_nova_conta(pessoa_fisica)
                else:
                    print("Operação falhou! O CPF não foi encontrado.")
                    
        elif listar_contas_op:

            nenhum_usuario = len(pessoas_fisicas) == 0
            if nenhum_usuario:
                print("Operação falhou! Cadastre uma Pessoa Física primeiro!\n")
            else:
                cpf = str(input("Informe o CPF: "))
                if existe_pessoa_fisica(pessoas_fisicas, cpf):
                    pessoa_fisica = consultar_pessoa_fisica(pessoas_fisicas, cpf)
                    listar_contas(pessoa_fisica)
                else:
                    print("Operação falhou! O CPF não foi encontrado.")

        elif novo_usuario:

            usuario = criar_novo_usuario()
            pessoas_fisicas.append(usuario)

        elif sair:

            print("\nObrigado e volte sempre!\n")
            break
        
        else:
            print("Opção inválida! Tente novamente.\n\n")



main()
