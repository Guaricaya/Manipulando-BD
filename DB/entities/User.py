from ..configs.Base import Base
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.name}'
