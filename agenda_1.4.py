def salvar_contatos(lista):
    arquivo = open('contatos.txt', 'w')

    for contato in lista:
        arquivo.write('{}#{}#{}\n'.format(
            contato['nome'], contato['email'], contato['telefone']))

    arquivo.close()


def carregar_contatos():
    lista = []

    try:
        arquivo = open('contatos.txt', 'r')

        for linha in arquivo.readlines():
            coluna = linha.strip().split('#')

            contato = {
                'email': coluna[1],
                'nome': coluna[0],
                'telefone': coluna[2]
            }

            lista.append(contato)

        arquivo.close()
    except FileNotFoundError:
        pass

    return lista


def existe_contato(lista, email):
    if len(lista) > 0:
        for contato in lista:
            if contato['email'] == email:
                return True
    return False


def adicionar(lista):

    while True:
        email = input('Digite o email do contato: ')

        if not existe_contato(lista, email):
            break
        else:
            print('Esse email ja foi utilizado')
            print('Por favor, tente um novo email')

    contato = {
        'email': email,
        'nome': input('Digite o nome:'),
        'telefone': input('Digite o telefone: ')
    }

    lista.append(contato)

    print('O contato {} foi cadastrado com sucesso! \n'.format(
        contato['nome']))


def alterar(lista):
    print(' == Alterar contatos == ')
    if len(lista) > 0:
        email = input('Digite o email do contato que quer alterar: ')
        if existe_contato(lista, email):
            for contato in (lista):
                if contato['email'] == email:
                    print('Nome: {}'.format(contato['nome']))
                    print('Email: {}'.format(contato['email']))
                    print('Telefone: {}'.format(contato['telefone']))

                    contato['nome'] = input('Digite o novo nome do contato: ')
                    contato['telefone'] = input(
                        'Digite o novo telefone do contato: ')
                    print('Os dados do contato {} foram alterados com sucesso'.format(
                        contato['email']))
                    break
        else:
            print(
                'Não existe nenhum contato cadastrado no sistema com o email {}.\n'.format(email))
    else:
        print('Não existe nenhum contato cadastrado no sistema.')


def excluir(lista):
    print(' == Excluir contatos == ')
    if len(lista) > 0:
        email = input('Digite o email do contato a ser excluido: ')
        if existe_contato(lista, email):
            for i, contato in enumerate(lista):
                if contato['email'] == email:
                    print('Nome: {}'.format(contato['nome']))
                    print('Email: {}'.format(contato['email']))
                    print('Telefone: {}'.format(contato['telefone']))

                    del lista[i]

                    print('O contato {} foi apagado com sucesso.'.format(
                        contato['nome']))
                    break
        else:
            print(
                'Não existe nenhum contato cadastrado no sistema com o email {}.\n'.format(email))
    else:
        print('Não existe nenhum contato cadastrado no sistema.')


def buscar(lista):
    print(' == Buscar contatos == ')
    if len(lista) > 0:
        email = input('Digite o email do contato que quer encontrar: ')
        if existe_contato(lista, email):
            for contato in (lista):
                if contato['email'] == email:
                    print('Nome: {}'.format(contato['nome']))
                    print('Email: {}'.format(contato['email']))
                    print('Telefone: {}'.format(contato['telefone']))
                    break
        else:
            print(
                'Não existe nenhum contato cadastrado no sistema com o email {}.\n'.format(email))
    else:
        print('Não existe nenhum contato cadastrado no sistema.')


def listar(lista):
    print(' == Lista de contatos == ')
    if len(lista) > 0:
        for i, contato in enumerate(lista):
            print('Contato {}:'.format(i+1))
            print('\tNome: {}'.format(contato['nome']))
            print('\tEmail: {}'.format(contato['email']))
            print('\tTelefone: {}'.format(contato['telefone']))
        print('Quantidade de contatos: {}\n'.format(len(lista)))
    else:
        print('Não existe nenhum contato cadastrado no sistema.\n')


def menu():

    lista = carregar_contatos()  # inicializa a lista de contatos

    while True:
        print('--- Agenda telefônica ---')
        print('1 - Adicionar contato')
        print('2 - Alterar contato')
        print('3 - Excluir contato')
        print('4 - Buscar contato')
        print('5 - Listar contatos')
        print('6 - Sair')
        opcao = int(input('>'))

        if opcao == 1:
            adicionar(lista)
            salvar_contatos(lista)
        elif opcao == 2:
            alterar(lista)
            salvar_contatos(lista)
        elif opcao == 3:
            excluir(lista)
            salvar_contatos(lista)
        elif opcao == 4:
            buscar(lista)
        elif opcao == 5:
            listar(lista)
        elif opcao == 6:
            print('Saindo do programa...')
            break
        else:
            print('Opcão inválida. Tente novamente.')


menu()
