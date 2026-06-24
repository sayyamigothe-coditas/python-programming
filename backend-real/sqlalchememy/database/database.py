#sqlalchemy with pydantic

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base


#first of all craete a engine for the db every engine have  session
engine=create_engine(
    "sqlite:///users.db",
    connect_args={"check_same_thread":False},
#"A connection can only be used in the thread where it was created
)

SessionLocal = sessionmaker(bind=engine)

#base is to derived a table
Base = declarative_base()



class UserTable(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)

#SQLAlchemy looks at every model registered in Base.metadata and creates the corresponding tables in the database if they do not already exist.
Base.metadata.create_all(bind=engine)

