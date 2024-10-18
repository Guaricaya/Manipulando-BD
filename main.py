from test import *

session = criar_conexao('''sqlite:///db1.db ''')

user = User(name = 'Filipe',password = '0482787034')
tabela = User
consulta = session.execute('''Select *
                From User''')
for row in consulta:
    print(row)
#create_user(session, user)
#user1 = read_user(session, tabela)[1]
#print(user1.password)
