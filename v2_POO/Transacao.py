from abc import *
from datetime import datetime
from Conta import Conta

class Transacao(ABC):

    @property
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(conta: Conta):
        pass


class Deposito(Transacao):
    _valor : float

    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
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

    def registrar(self, conta: Conta):
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
                "tipo": transacao.__str__.__name__,
                "valor": transacao._valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )