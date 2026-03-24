import sqlalchemy
from database import metadata

contas = sqlalchemy.Table(
    'conta',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key = True, autoincrement= True),
    sqlalchemy.Column('saldo', sqlalchemy.Float, nullable= False),
    sqlalchemy.Column('cliente_id', sqlalchemy.Integer, sqlalchemy.ForeignKey("cliente.id", ondelete= "CASCADE"))
    
)