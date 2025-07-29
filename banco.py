from cliente import Cliente
from cliente_existente_exception import ClienteExistenteException


class Banco:

    def __init__(self):
        self.__contas = []
        self.__clientes = []

    def cadastrar_cliente(self, codigo, cpf, nome):
        for cliente in self.__clientes:
            if cpf == cliente.cpf:
                raise ClienteExistenteException('O cliente de cpf ' + cpf + ' já cadastrado!')
        cliente = Cliente(codigo, cpf, nome)
        self.__clientes.append(cliente)

    def listar_clientes(self):
        return self.__clientes

