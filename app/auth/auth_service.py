from datetime import datetime, UTC

from sqlalchemy.orm import Session

from app.auth.jwt import create_access_token
from app.auth.password import verify_password
from app.auth.schemas import LoginRequest, TokenResponse
from app.exceptions.user import InvalidCredentialsError
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, session: Session):
        self.user_repository = UserRepository(session)

    def login(self, request: LoginRequest) -> TokenResponse:
        user = self.user_repository.get_by_email(request.email)

        if user is None:
            raise InvalidCredentialsError()

        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise InvalidCredentialsError()

        user.last_login = datetime.now(UTC)

        self.user_repository.commit()

        access_token = create_access_token(
            {
                "sub": str(user.id),
            }
        )

        return TokenResponse(
            access_token=access_token,
            token_type="Bearer",
        )