from fastapi import status
from app.exceptions.base import BusinessException


class UserAlreadyExistsError(BusinessException):
    """
    Raised when a user with the given email already exists.
    """

    def __init__(self, email: str):
        super().__init__(
            message=f"User with email '{email}' already exists.",
            status_code=status.HTTP_409_CONFLICT,
        )