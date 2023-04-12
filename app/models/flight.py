from pydantic import BaseModel

class Flight(BaseModel):
    FLIGHT_ID: int
    AIRLINE_ID: int
    AIRLINE_NAME: str
    TO_LOCATION: str
    LOCAL_SEATS: int

class FlightUpdate(BaseModel):
    AIRLINE_ID: int
    AIRLINE_NAME: str
    TO_LOCATION: str
    LOCAL_SEATS: int

