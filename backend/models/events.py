from sqlalchemy import Column, String, Text, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from .base import Base

class Event(Base):
    __tablename__ = "events"
    __table_args__ = {"schema": "core"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text)
    location = Column(Text, nullable=False)
    start_datetime = Column(TIMESTAMP(timezone=True), nullable=False)
    end_datetime = Column(TIMESTAMP(timezone=True), nullable=False)
    is_ticket_available = Column(Boolean, nullable=False, default=True)
    created_by = Column(UUID(as_uuid=True), ForeignKey("core.users.id"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    creator = relationship("User", back_populates="created_events")
    tickets = relationship("Ticket", back_populates="event", cascade="all, delete-orphan")