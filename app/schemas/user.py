from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    """
    Request model for creating a user.
    """

    first_name: str
    last_name: str
    email: EmailStr


class UserResponse(BaseModel):
    """
    Response model for returning user data.
    """

    id: int
    first_name: str
    last_name: str
    email: EmailStr
    created_at: datetime
    last_login: datetime
    model_config = ConfigDict(from_attributes=True)