
from cliente import Cliente
from conta import Conta

# == test-drive ==

cliente1 = Cliente('1', '706', 'Pedro Nóbrega')
conta1 = Conta('1', cliente1)
conta1.saldo = 1000
print(conta1.saldo)
print(conta1.numero)
print(conta1.cliente)
