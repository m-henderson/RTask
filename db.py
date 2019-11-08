from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'postgresql://postgres:RobedCoder@localhost:5432/rtask'
engine = create_engine('postgresql://postgres:RobedCoder@localhost:5432/rtask')
Base = declarative_base(engine)
db_session = sessionmaker(bind=engine)


# import models after base is declared
from models import ticket

def init_db():
    #Base.create_all(engine)
    print('hey')

