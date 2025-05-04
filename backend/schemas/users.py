from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime
from models import UserRole



class UserBase(BaseModel):
    username: str = Field(
        ..., min_length=3, 
        max_length=50,
        description="Unique username of the user",
        example="john_doe",
    )
    email: EmailStr = Field(
        ...,
        description="Email address of the user",
        example="sample_email@sample.com",
    )
    role: UserRole = Field(
        UserRole.client,
        description="Role of the user. Must be one of: " + ", ".join([f"'{item.value}'" for item in UserRole]),
        example=UserRole.client,
    )
    
    class Config:
        from_attributes = True



class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        description="Password for the user",
        example="securepassword123",
    )


class UserResponse(UserBase):
    id: UUID = Field(
        ...,
        description="Unique identifier for the user",
        example="123e4567-e89b-12d3-a456-426614174000",
    )
    created_at: datetime = Field(
        ...,
        description="Timestamp when the user was created",
        example="2023-10-01T12:00:00Z",
    )
    is_active: bool = Field(
        True,
        description="Indicates if the user is active",
        example=True,
    )


