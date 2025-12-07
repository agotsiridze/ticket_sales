from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime
from enums import UserRole


class UserBase(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Unique username of the user",
        examples=["john_doe"],
    )
    email: EmailStr = Field(
        ...,
        description="Email address of the user",
        examples=["sample_email@sample.com"],
    )
    role: UserRole = Field(
        UserRole.client,
        description="Role of the user. Must be one of: "
        + ", ".join([f"'{item.value}'" for item in UserRole]),
        examples=[UserRole.client],
    )

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        description="Password for the user",
        examples=["securepassword123"],
    )


class UserResponse(UserBase):
    id: UUID = Field(
        ...,
        description="Unique identifier for the user",
        examples=["123e4567-e89b-12d3-a456-426614174000"],
    )
    created_at: datetime = Field(
        ...,
        description="Timestamp when the user was created",
        examples=["2023-10-01T12:00:00Z"],
    )
    is_active: bool = Field(
        True,
        description="Indicates if the user is active",
        examples=[True],
    )


class UserFilter(BaseModel):
    """Query parameters for filtering users"""

    username: str | None = Field(
        None,
        description="Filter by username (partial match)",
        examples=["john"],
    )
    email: str | None = Field(
        None,
        description="Filter by email (partial match)",
        examples=["sample@"],
    )
