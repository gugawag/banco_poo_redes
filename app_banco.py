import sys

from banco import Banco
from cliente_existente_exception import ClienteExistenteException

bancoIF = Banco()
prox_codigo_cliente = 1

def imprimir_clientes():
    for cliente in bancoIF.listar_clientes():
        print(cliente)

def menu():
    print("0 - Sair")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Remover Cliente")
    print("4 - Cadastrar Conta")
    print("5 - Listar Contas")
    print("6 - Remover Conta")

while True:
    menu()
    opcao = int(input('\nDigite uma opção:'))

    match opcao:
        case 0:
            sys.exit()
        case 1:
            cpf = input('Digite o CPF:')
            nome = input('Digite o nome:')
            try:
                bancoIF.cadastrar_cliente(str(prox_codigo_cliente), cpf, nome)
                prox_codigo_cliente += 1
            except ClienteExistenteException:
                print('Cliente já cadastrado com esse CPF')

        case 2:
            print('=== Listagem Clientes ===')
            if len(bancoIF.listar_clientes()) == 0:
                print('Não há clientes cadastrados!')
            imprimir_clientes()



