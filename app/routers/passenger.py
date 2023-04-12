from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, PassengerProfile
from fastapi.encoders import jsonable_encoder
from models import passenger as passenger_model

router = APIRouter(
    prefix="/passenger",
    tags=["passenger"],
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
def get_passengers(db: Session = Depends(get_db)):
    all_records = db.query(PassengerProfile).all()
    return jsonable_encoder(all_records)

@router.post("/")
def create_passenger(passenger: passenger_model.PassengerProfile, db: Session = Depends(get_db)):
    passenger = PassengerProfile(**passenger.dict())
    db.add(passenger)
    db.commit()
    return {"message": "Passenger created"}

@router.delete("/{profile_id}")
def delete_passenger(profile_id: int, db: Session = Depends(get_db)):
    passenger = db.query(PassengerProfile).filter(PassengerProfile.PROFILE_ID == profile_id).first()
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    db.delete(passenger)
    db.commit()
    return {"message": f"Passenger {passenger.PROFILE_ID} deleted successfully"}