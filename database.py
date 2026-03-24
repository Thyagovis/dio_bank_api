import sqlalchemy as sa
import databases
from sqlalchemy import event
from sqlalchemy.pool import StaticPool

DATABASE_URL = "sqlite:///./bank.db"

database =  databases.Database(DATABASE_URL)
metadata = sa.MetaData()

engine = sa.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()