from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

DB_URL = 'postgresql://sagor:password@localhost/fastapidb'

engine = create_engine(DB_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
