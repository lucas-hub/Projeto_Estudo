#! python

agenda_estados = {'Lucas': 'Sao Paulo',
          'Maria': 'Sao Paulo',
          'Gabriel': 'Rio de Janeiro',
          'Renata': 'Minas Gerais'}

agenda_telefone = {'Lucas': '92123-9823',
          'Maria': '92341-2874',
          'Gabriel': '94824-7823',
          'Renata': '92764-1892'}

def achar_estado():
    nome = str(input('insira o nome da pessoa que quer consultar o estado e o telefone: '))
    print(f'Essa pessoa mora em: {agenda_estados[nome]} e tem o telefone: {agenda_telefone[nome]}.')

if __name__ == '__main__':
    achar_estado()
