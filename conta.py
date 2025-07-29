from cliente import Cliente

class Conta:

    # saldo, numero, cliente
    def __init__(self, numero, cliente, saldo=0.0):
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero

    @property
    def cliente(self):
        return self.__cliente

    def creditar(self, valor):
        self.__validar_valor_negativo(valor)
        self.__saldo += valor

    def debitar(self, valor):
        self.__validar_valor_negativo(valor)
        self.__saldo -= valor

    def __validar_valor_negativo(self, valor):
        if valor < 0:
            raise ValueError('Valor negativo!')

    def transferir(self, destino, valor):
        self.debitar(valor)
        destino.creditar(valor)











