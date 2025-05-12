from uuid import uuid4
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    ForeignKey,
    Enum,
    Index,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base
from enums import TicketStatus


class Ticket(Base):
    __tablename__ = "tickets"
    __table_args__ = (
        Index("idx_tickets_event_id", "event_id"),
        Index("idx_tickets_owner_id", "owner_id"),
        Index("idx_tickets_status", "status"),
        Index("idx_tickets_created_at", "created_at"),
        {"schema": "core"},
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    event_id = Column(
        UUID(as_uuid=True),
        ForeignKey("core.events.id", ondelete="CASCADE"),
        nullable=False
    )

    owner_id = Column(
        UUID(as_uuid=True),
        ForeignKey("core.users.id", ondelete="SET NULL"),
        nullable=True
    )

    status = Column(Enum(TicketStatus, name="ticketstatus"), nullable=False, default=TicketStatus.available)

    price = Column(Integer, nullable=False)
    access_level = Column(String, nullable=True)
    seat = Column(String, nullable=True)
    room = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    expiry_datetime = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    event = relationship("Event", back_populates="tickets", lazy="selectin")
    owner = relationship("User", back_populates="tickets", lazy="selectin")