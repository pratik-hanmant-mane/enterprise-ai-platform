from typing import Generator

from sqlalchemy.orm import Session, sessionmaker

from app.db.engine import engine


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_db() -> Generator[Session, None, None]:
    """
    Creates a database session for each request.

    The session is automatically closed after the request completes.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()