from uuid import uuid4
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base
from.enums import TicketStatus




class Ticket(Base):
    __tablename__ = "tickets"
    __table_args__ = {"schema": "core"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    event_id = Column(UUID(as_uuid=True), ForeignKey("core.events.id"), nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("core.users.id"), nullable=True)
    status = Column(Enum(TicketStatus), nullable=False, default=TicketStatus.available)
    price = Column(Integer, nullable=False)
    access_level = Column(String, nullable=True)
    seat = Column(String, nullable=True)
    room = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    expiry_datetime = Column(DateTime, nullable=True)
    
    event = relationship("Event", back_populates="tickets")
    owner = relationship("User", back_populates="tickets")