from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from models import UserRole



class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: UserRole
    
    class Config:
        from_attributes = True



class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    is_active: bool


