from app.auth.schemas import LoginRequest
from app.auth.jwt import create_access_token
from app.exceptions.user import InvalidCredentialsError
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, 
              request: LoginRequest) -> AccessToken:
        email = request.email
        password = request.password
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise InvalidCredentialsError
        if not user.check_password(password):
            raise InvalidCredentialsError
        return create_access_token(user.id)