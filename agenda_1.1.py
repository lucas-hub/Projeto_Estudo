#! python

Lucas = {}

Lucas['PrimeiroNome'] = 'Lucas'
Lucas['Sobrenome'] = 'Marco'
Lucas['Idade'] = '21'
Lucas['Cidade'] = 'Sao Paulo'
Lucas['Telefone'] = '92387-1289'

def dados():
    pessoa = str(input('Digite a pessoa que quer acessar os dados: '))
    if pessoa == 'Lucas':
        dado = str(input('Agora, qual dado quer obter: '))
        resultado = Lucas[dado]
    if pessoa != 'Lucas':
        print('Nome inválido')
    return print(resultado)


if __name__ == '__main__':
    dados()   


