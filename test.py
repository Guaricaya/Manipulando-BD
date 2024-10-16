from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def criar_conecao(bd_link:str):
    engine = create_engine(bd_link, echo=True)
    Session = sessionmaker(bind=engine)
    

    Base.metadata.create_all(engine)

    return Session()
    
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.name}'




def create_user(session, user):
    session.add(user)
    session.commit()

def read_user(session, tabela):
    resultado = session.query(tabela).all()
    
    return resultado
    
    
def delete_user(session, user):
    session.delete(read_user(session,user))
    session.commit()

def delete_all_user(session, user):
    for usuario in read_user(session,user):
        session.delete(usuario)
    session.commit()


