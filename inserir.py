from criarTabela import Pessoas, session


"""
Inserir no banco:
"""
# abaixo, a cada instância, é também inserido uma instância no banco de dados
pessoa1 = Pessoas(nome="Marcus", email="marcus@outlook.com", idade=100)

# como a sessão controla a conexão:
#session.add(pessoa1)
session.add_all([pessoa1])
session.commit()  # persiste os dados

# limpar a sessão:
session.flush()
