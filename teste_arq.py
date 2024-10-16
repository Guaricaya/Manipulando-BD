from DB.repository.user_repository import UserRespository
repo = UserRespository()
repo.delete_user_by_name(['Filipe'])
data = repo.read_user_all()
print(data)