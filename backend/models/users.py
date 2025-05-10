import uuid
from sqlalchemy import (
    Column,
    String,
    Text,
    Boolean,
    Enum,
    TIMESTAMP,
    Index,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base
from enums import UserRole


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        Index("idx_users_email", "email"),
        Index("idx_users_username", "username"),
        Index("idx_users_is_active", "is_active"),
        {"schema": "core"},
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    email = Column(Text, nullable=False, unique=True)
    password_hash = Column(Text, nullable=False)
    role = Column(Enum(UserRole, name="userrole"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    is_active = Column(Boolean, default=True, nullable=False)

    created_events = relationship("Event", back_populates="creator", lazy="selectin")
    tickets = relationship("Ticket", back_populates="owner", lazy="selectin")