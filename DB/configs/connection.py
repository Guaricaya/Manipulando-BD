from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = '''sqlite:///db1.db '''
        self.__engine = self.__create_engine()
        self.session = None
        pass

    def __create_engine(self):
        engine = create_engine(self.__connection_string, echo=True)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker(bind= self.__engine)
        self.session = session_maker()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()