from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

from enums import TicketStatus




class TicketBase(BaseModel):
    price: int = Field(
        description="Price of the ticket in cents",
        examples=[1000, 5000, 3000],
    )
    access_level: str | None = Field(
        default=None,
        description="Access level of the ticket. (Optional)",
        examples=["VIP","ECONOMY", "STUFF"],
    )
    seat: str | None = Field(
        default=None,
        description="Seat number for the ticket. (Optional)",
        examples=["A1", "B2", "C3"],
    )
    room: str | None = Field(
        default=None,
        description="Room or hall identifier for the ticket. (Optional)",
        examples=["Main Hall", "VIP Lounge", "Conference Room"],
    )
    expiry_datetime: datetime | None = Field(
        default=None,
        description="Expiry date and time of the ticket. (Optional)",
        examples=["2025-05-01"],
    )

    class Config:
        from_attributes = True


class TicketCreate(TicketBase):
    pass


class TicketRead(TicketBase):
    id: UUID = Field(
        ...,
        description="Unique identifier for the ticket",
        examples=["123e4567-e89b-12d3-a456-426614174000"]
    )
    created_at: datetime = Field(
        ...,
        description="Timestamp when the ticket was created",
        examples=["2023-10-01"]
    )
    status: TicketStatus = Field(
        examples=[TicketStatus.available],
        description="Current status of the ticket. Must be one of: " + ", ".join([f"'{item.value}'" for item in TicketStatus]),
    )
    owner_id: UUID | None = Field(
        default=None,
        description="Unique identifier of the user who owns the ticket. (Optional)",
        examples=["123e4567-e89b-12d3-a456-426614174000"]
    )
    event_id: UUID = Field(
        ...,
        description="Unique identifier of the event associated with the ticket",
        examples=["123e4567-e89b-12d3-a456-426614174000"]
    )


class TicketFilter(BaseModel):
    status: TicketStatus | None = Field(
        default=None,
        examples=[TicketStatus.available],
        description="Current status of the ticket. Must be null or one of: " + ", ".join([f"'{item.value}'" for item in TicketStatus]),
    )
    owner_id: UUID | None = Field(
        default=None,
        description="Unique identifier of the user who owns the ticket. (Optional)",
        examples=["123e4567-e89b-12d3-a456-426614174000"]
    )
    access_level: str | None = Field(
        default=None,
        description="Access level of the ticket. (Optional)",
        examples=["VIP","ECONOMY", "STUFF"],
    )
    room: str | None = Field(
        default=None,
        description="Room or hall identifier for the ticket. (Optional)",
        examples=["Main Hall", "VIP Lounge", "Conference Room"],
    )


class TicketUpdate(BaseModel):
    # Core update fields
    status: TicketStatus | None = Field(
        default=None,
        examples=[TicketStatus.available, TicketStatus.reserved],
        description="New status for the ticket."
    )
    owner_id: UUID | None = Field(
        default=None,
        description="New owner UUID. Setting to null means unclaiming the ticket."
    )

    price: int | None = Field(
        default=None,
        description="Price of the ticket in cents. (Optional update)"
    )
    access_level: str | None = Field(
        default=None,
        description="Access level of the ticket. (Optional update)"
    )
    seat: str | None = Field(
        default=None,
        description="Seat number for the ticket. (Optional update)"
    )
    room: str | None = Field(
        default=None,
        description="Room or hall identifier for the ticket. (Optional update)"
    )
    expiry_datetime: datetime | None = Field(
        default=None,
        description="Expiry date and time of the ticket. (Optional update)"
    )
