from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.exceptions.user import UserAlreadyExistsError
import logging
from app.db.session import get_db
logger = logging.getLogger(__name__)

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
        logger.info("Creating user")
        existing_user = self.user_repository.get_by_email(email)

        if existing_user:
            logger.warning(
                "Duplicate email detected."
            )
            raise UserAlreadyExistsError(email)

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        self.user_repository.create(user)
        logger.info("User created successfully")
        # Transaction boundary
        self.session.commit()
        logger.info("Transaction committed successfully")
        return user

    def get_user(   
        self,
        user_id: int,
    ):
        return self.user_repository.get_by_id(user_id)