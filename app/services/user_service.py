from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:
    """
    Business logic related to users.
    """

    def __init__(self, session: Session):
        self.session = session
        self.user_repository = UserRepository(session)

    def create_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
    ) -> User:
        """
        Create a new user.
        """

        existing_user = self.user_repository.get_by_email(email)

        if existing_user:
            raise ValueError(
                f"User with email '{email}' already exists."
            )

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        self.user_repository.create(user)

        # Transaction boundary
        self.session.commit()

        return user