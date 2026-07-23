from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.jwt import decode_access_token
from app.database.session import get_db
from app.models.user import User
from app.services.user_service import UserService

def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_db),
) -> User:
    try:
        payload = decode_access_token(token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired access token",
        )

    email = payload.get("sub")

    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )

    user = UserService(session).get_user_by_email(email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user