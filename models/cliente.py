import sqlalchemy
from database import metadata

clientes = sqlalchemy.Table(
    'cliente',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key = True, autoincrement= True),
    sqlalchemy.Column('cpf', sqlalchemy.String, nullable = False, unique= True),
    sqlalchemy.Column('nome', sqlalchemy.String, nullable = False),
    

)