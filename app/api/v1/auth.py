from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.auth.schemas import LoginRequest, TokenResponse
from app.auth.auth_service import AuthService


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    payload: LoginRequest,
    session: Session = Depends(get_db),
) -> TokenResponse:

    auth_service = AuthService(session)

    return auth_service.login(payload)