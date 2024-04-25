import datetime
from Conta import Conta
from Transacao import Transacao


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

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    
    _cpf: str
    _nome: str
    _data_nascimento: datetime.date

    def __init__(self, endereco, cpf, nome, dt):
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