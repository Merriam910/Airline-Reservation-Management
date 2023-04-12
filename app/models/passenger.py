from pydantic import BaseModel

class PassengerProfile(BaseModel):
    PROFILE_ID = int
    PASSWORD = int
    FIRST_NAME = str
    EMAIL_ADDRESS = str

class PassengerProfileUpdated(BaseModel):
    PASSWORD = int
    FIRST_NAME = str
    EMAIL_ADDRESS = str