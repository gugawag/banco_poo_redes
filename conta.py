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

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            raise ValueError('Não permitido saldo negativo!')
        self.__saldo = novo_saldo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero

    @property
    def cliente(self):
        return self.__cliente
