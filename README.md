# OBJECT RELATIONAL MODEL


Basicamente, ORM, é uma forma de unir orientacao a objetos ao SQL.
Nesse caso, classes tornar-se-ão instânicias no banco de dados.

É como se o ORM fosse um intermediário:

codigo -> ORM -> Banco de dados (Relacional)


SQLAlchemy é um dos ORM que existem, mas, é o mais usado.
Além disso, tem um conjunto de ferramentas para trabalhar com
diversos banco de dados relacionais.


### nomenclaturas:

1) Engine: parte responsável pela conexão do banco de dados
2) Sessão: chama a engine, é uma forma de manipular a interação da engine

### Tipos:
BigInteger => BigInt
Boolean => Boolean
Date => Date
Enum
Float
Integer
Numeric
LargeBinary => Blob
Text => CLOB

### Usos
1) criar a engine
2) criar sessao para conectar a engine
3) definir tabela com pk
4) criar banco

### instalação:
pip install sqlalchemy

### libs usadas:
pip install -r requirements
