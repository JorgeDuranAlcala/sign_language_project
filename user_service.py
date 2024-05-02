import users_repository
class UserService:
    def __init__(self):
        self.user_repository = users_repository.UsersRepository()

    def sign_in(self, email, password):
        return self.user_repository.find(email, password)

    def sign_up(self, email, password):
        user = {'email': email, 'password': password}
        return self.user_repository.insert(user)