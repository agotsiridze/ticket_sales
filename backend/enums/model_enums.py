from enum import Enum


class UserRole(str, Enum):
    organizer = "organizer"
    client = "client"
    admin = "admin"


class TicketStatus(Enum):
    available = "available"
    reserved = "reserved"
    paid = "paid"
