from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.base import BusinessException


class AuthError(BusinessException):
    """
    Raised when an authentication error occurs.
    """

    def __init__(self, message: str):
        super().__init__(
            message=message,
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

class InvalidCredentialsError(BusinessException):

    def __init__(self):
        super().__init__(
            message="Invalid email or password.",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )