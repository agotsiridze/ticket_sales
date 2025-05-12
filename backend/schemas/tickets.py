from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

from enums import TicketStatus




class TicketBase(BaseModel):
    price: int = Field(
        ...,
        description="Price of the ticket in cents",
        example=1000
    )

    access_level: str | None = Field(
        ...,
        description="Access level of the ticket. (Optional)",
        example="VIP"
    )
    seat: str | None = Field(
        ...,
        description="Seat number for the ticket. (Optional)",
        example="A1"
    )
    room: str | None = Field(
        ...,
        description="Room or hall identifier for the ticket. (Optional)",
        example="Main Hall"
    )
    expiry_datetime: datetime | None = Field(
        ...,
        description="Expiry date and time of the ticket. (Optional)",
        example="2025-05-01"
    )

    class Config:
        from_attributes = True


class TicketCreate(TicketBase):
    pass


class TicketRead(TicketBase):
    id: UUID = Field(
        ...,
        description="Unique identifier for the ticket",
        example="123e4567-e89b-12d3-a456-426614174000"
    )
    created_at: datetime = Field(
        ...,
        description="Timestamp when the ticket was created",
        example="2023-10-01"
    )
    status: TicketStatus = Field(
        example=TicketStatus.available,
        description="Current status of the ticket. Must be one of: " + ", ".join([f"'{item.value}'" for item in TicketStatus]),
    )
    owner_id: UUID | None = Field(
        ...,
        description="Unique identifier of the user who owns the ticket. (Optional)",
        example="123e4567-e89b-12d3-a456-426614174000"
    )
    event_id: UUID = Field(
        ...,
        description="Unique identifier of the event associated with the ticket",
        example="123e4567-e89b-12d3-a456-426614174000"
    )