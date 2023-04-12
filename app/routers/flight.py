from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Flight
from fastapi.encoders import jsonable_encoder
from models import flight as flight_model

router = APIRouter(
    prefix="/flight",
    tags=["flight"],
    responses={404: {"description": "Not found"}},
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_flights(db: Session = Depends(get_db)):
    all_records = db.query(Flight).all()
    return jsonable_encoder(all_records)

@router.post("/")
def create_flight(flight: flight_model.Flight, db: Session = Depends(get_db)):
    flight = Flight(**flight.dict())
    db.add(flight)
    db.commit()
    return {"message": "Flight created"}

@router.delete("/{flight_id}")
def delete_flight(flight_id: int, db: Session = Depends(get_db)):
    flight = db.query(Flight).filter(Flight.FLIGHT_ID == flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    db.delete(flight)
    db.commit()
    return {"message": f"Flight {flight_id.FLIGHT_ID} deleted successfully"}


@router.put("/{flight_id}")
def update_flight(flight_id: int, updated_flight: flight_model.FlightUpdate, db: Session = Depends(get_db)):
    flight = db.query(Flight).filter(Flight.FLIGHT_ID == flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")

    # TODO: improve this
    flight.AIRLINE_ID = updated_flight.AIRLINE_ID
    flight.AIRLINE_NAME = updated_flight.AIRLINE_NAME
    flight.LOCAL_SEATS = updated_flight.LOCAL_SEATS
    flight.TO_LOCATION = updated_flight.TO_LOCATION

    db.add(flight)
    db.commit()
    return {"message": f"Flight {flight.FLIGHT_ID} updated successfully"}