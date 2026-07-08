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
        print(self.user_repository)