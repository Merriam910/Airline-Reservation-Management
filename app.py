from typing import Union
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from database import session, Flight, PassengerProfile, TicketInfo

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "AIRLINE MANAGEMENT SYSTEM"}


@app.get("/flights")
def get_flights():
    all_records = session.query(Flight).all()
    return jsonable_encoder(all_records)

@app.get("/tickets")
def get_tickets():
    all_records = session.query(TicketInfo).all()
    return jsonable_encoder(all_records)

@app.get("/passengers")
def get_passengers():
    all_records = session.query(PassengerProfile).all()
    return jsonable_encoder(all_records)


@app.post("/flights")
def create_flight(FLIGHT_ID: int, AIRLINE_ID: int, AIRLINE_NAME: str, TO_LOCATION: str, LOCAL_SEATS: int):
    flight = Flight(FLIGHT_ID=FLIGHT_ID, AIRLINE_ID=AIRLINE_ID, AIRLINE_NAME=AIRLINE_NAME, TO_LOCATION=TO_LOCATION, LOCAL_SEATS=LOCAL_SEATS)
    session.add(flight)
    session.commit()
    return {"message": "Flight created"}

@app.post("/tickets")
def create_ticket(TICKET_ID: str, FLIGHT_ID: str, PROFILE_ID: str, STATUS: str):
    ticket = TicketInfo(TICKET_ID=TICKET_ID, FLIGHT_ID=FLIGHT_ID, PROFILE_ID=PROFILE_ID, STATUS=STATUS)
    session.add(ticket)
    session.commit()
    return {"message": "Ticket created"}

@app.delete("/flights/{flight_id}")
def delete_flight(flight_id: int):
    flight = session.query(Flight).filter(Flight.FLIGHT_ID == flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    session.delete(flight)
    session.commit()
    return {"message": f"Flight {flight_id.FLIGHT_ID} deleted successfully"}

@app.delete("/ticket/{ticket_id}")
def delete_ticket(ticket_id: int):
    ticket = session.query(TicketInfo).filter(TicketInfo.TICKET_ID == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    session.delete(ticket)
    session.commit()
    return {"message": f"Ticket {ticket.TICKET_ID} deleted successfully"}

@app.delete("/passenger/{profile_id}")
def delete_flight(profile_id: int):
    passenger = session.query(PassengerProfile).filter(PassengerProfile.PROFILE_ID == profile_id).first()
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    session.delete(passenger)
    session.commit()
    return {"message": f"Passenger {passenger.PROFILE_ID} deleted successfully"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
