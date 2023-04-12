from pydantic import BaseModel

class TicketInfo(BaseModel):
    TICKET_ID = int
    FLIGHT_ID = int
    PROFILE_ID = int
    STATUS = str

class TicketInfoUpdate(BaseModel):
    FLIGHT_ID = int
    PROFILE_ID = int
    STATUS = str

