from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("postgresql://postgres:postgres@localhost:5432/user_db")

Session = sessionmaker(bind=engine)
