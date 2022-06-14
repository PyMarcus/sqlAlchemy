from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# configurações básicas:
engine = create_engine("sqlite:///teste.db", echo=True)  # cria um banco sqlite(já vem no python) e echo informa o q fez
Session = sessionmaker(bind=engine)  # retorna uma classe, a sessão aponta para a engine(conexao) criada
session = Session()  # session recebe a instância
Base = declarative_base()  # banco de dados


class Pessoas(Base):
    """
    Classe que representará um tabela no banco de dados
    Ao ser definido uma pk, a linha Base.metadata é executada
    criando o banco
    """
    __tablename__ = 'pessoas'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    email: str = Column(String)
    idade: int = Column(Integer)

    def __repr__(self) -> str:
        return f"Pessoa(nome={self.nome}, idade={self.idade}, email={self.email}"  # representacao para nao exibir
        # endereço de memória


if __name__ == '__main__':
    Base.metadata.create_all(engine)  # cria o banco e conecta a engine
