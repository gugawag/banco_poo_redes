class Cliente:

    def __init__(self, codigo, cpf, nome):
        self.__codigo = codigo
        self.__cpf = cpf
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return 'Código:' + self.__codigo + 'Nome:' + self.__nome + ' CPF:' + self.__cpf
