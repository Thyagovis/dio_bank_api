import sqlalchemy
from database import metadata

transacoes = sqlalchemy.Table(
    'transacao',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key= True, autoincrement= True),
    sqlalchemy.Column('conta_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('conta.id', ondelete= "CASCADE")),
    sqlalchemy.Column('tipo_transacao', sqlalchemy.String, nullable= False),
    sqlalchemy.Column('valor', sqlalchemy.Float, nullable= False)
    
)