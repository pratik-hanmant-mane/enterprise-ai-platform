from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    """
    Repository for User-specific database operations.
    """

    def __init__(self, session: Session):
        super().__init__(session, User)

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        """
        Retrieve a user by email.
        """
        stmt = select(User).where(User.email == email)
        return self.session.scalar(stmt)

    def last_login(
        self,
        user_id: int,
    ) -> None:
        """
        Update the last login timestamp for a user.
        """
        stmt = update(User).where(User.id == user_id).values(last_login=datetime.utcnow())
        self.session.execute(stmt)
        self.session.commit()