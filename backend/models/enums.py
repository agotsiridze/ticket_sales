from enum import Enum

class UserRole(str, Enum):
    organizer = "organizer"
    client = "client"
    
class TicketStatus(Enum):
    available = "available"
    reserved = "reserved"
    paid = "paid"