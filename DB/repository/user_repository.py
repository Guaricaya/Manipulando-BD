from ..configs.connection import DBConnectionHandler
from ..entities.User import User


# Aqui ficara as operações no Banco de Dados (CRUD) 
class UserRespository:
    def create_user(self,user:User)->None:
        with DBConnectionHandler() as DB:
            DB.session.add(user)
            DB.session.commit()

    def read_user(self, tabela):
        with DBConnectionHandler() as DB:
            resultado = DB.session.query(tabela).all()
            return resultado

    def read_user_all(self):
        with DBConnectionHandler() as DB:
            resultado = DB.session.query(User).all()
            return resultado    
        
    def delete_user_by_name(self, name_list:list)->None:
        with DBConnectionHandler() as DB:
            for name in name_list:
                DB.session.query(User).filter(User.name == name).delete()
            DB.session.commit()

    def update_user(self, name, senha):
        
        with DBConnectionHandler() as DB:
            DB.session.query(User).filter(User.name == name).update({'passward':senha})
            DB.session.commit()

    '''def delete_all_user(self, user):
        with DBConnectionHandler() as DB:
            for usuario in self.read_user(user):
                DB.session.delete(usuario)
            DB.session.commit()'''