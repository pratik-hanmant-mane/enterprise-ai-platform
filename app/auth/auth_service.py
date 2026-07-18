from app.auth.schemas import LoginRequest
from app.auth.jwt import create_access_token
from app.exceptions.user import InvalidCredentialsError
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

def login(request: LoginRequest) -> TokenResponse:

    user = UserRepository.get_by_email(request.email)

    if user is None:
        raise InvalidCredentialsError()

    if not verify_password(
        request.password,
        user.password_hash,
    ):
        raise InvalidCredentialsError()

    payload = {
        "sub": str(user.id),
    }
    user.last_login = datetime.utcnow()
    UserRepository.session.commit()
    access_token = create_access_token(payload)
    return TokenResponse(
        access_token=access_token,
        token_type="Bearer",
    )