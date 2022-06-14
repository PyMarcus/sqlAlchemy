from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine as ce
from criarTabela import session, Pessoas


engine = ce("sqlite:///teste.db")
db = scoped_session(sessionmaker(bind=engine))

# forma mais efetiva:
items = db.execute("select * from pessoas").fetchall()
print(items)

# forma rápida de consulta , mas , a de cima é melhor
items = session.query(Pessoas).all()
print(items)
