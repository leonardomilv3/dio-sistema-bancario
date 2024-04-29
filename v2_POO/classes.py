from abc import *
from datetime import datetime


class Transacao(ABC):

    @property
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(conta):
        pass


class Deposito(Transacao):
    _valor : float

    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def __str__(self) -> str:
        return "Depósito"

    def registrar(self, conta):
        sucesso_deposito = conta.depositar(self.valor)

        if sucesso_deposito:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    _valor : float

    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor
    
    def __str__(self) -> str:
        return "Saque"

    def registrar(self, conta):
        sucesso_saque = conta.sacar(self.valor)

        if sucesso_saque:
            conta.historico.adicionar_transacao(self)
    



class Historico():
    
    _transacoes : list

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes 
    

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )


class Cliente():

    _endereco: str
    _contas: list

    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco
    
    @property
    def contas(self):
        return self._contas

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def realizar_transacao(self, conta, transacao: Transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    
    _cpf: str
    _nome: str
    _data_nascimento: datetime.date

    def __init__(self, cpf, nome, dt, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = dt
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome


class Conta():

    _saldo : float
    _numero : int
    _agencia : str
    _cliente : Cliente
    _historico : Historico

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    


    def sacar(self, valor: float) -> bool:
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(f"Operação falhou! O valor: {valor:.2f} excedeu o saldo: {saldo:.2f}.\n")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!\n")
            return True
        else:
            print("Operação falhou! O valor informado não é válido!\n")

        return False

    def depositar(self, valor: float) -> bool:
        
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("Operação falhou! O valor informado não é válido!\n")

        return False
    

class ContaCorrente(Conta):

    _limite : float
    _limite_saques : int

    def __init__(self, numero, cliente, lim=500, lim_saq=3):
        super().__init__(numero, cliente)
        self._limite = lim
        self._limite_saques = lim_saq

    @property
    def limite(self):
        return self._limite
    
    @property
    def limite_saques(self):
        return self._limite_saques

    def sacar(self, valor):

        numeros_saques = len([transacao for transacao in self.historico._transacoes if transacao["tipo"] == Saque.__name__ ])

        excedeu_limite = valor > self.limite
        excedeu_saques = numeros_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor é maior que o limite da conta.")
        elif excedeu_saques:
            print("Operação falhou! O limite de saques diários da conta foi atingido.")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
