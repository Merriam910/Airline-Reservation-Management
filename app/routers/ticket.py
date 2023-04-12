from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, TicketInfo
from fastapi.encoders import jsonable_encoder
from models import ticket as ticket_model

router = APIRouter(
    prefix="/ticket",
    tags=["ticket"],
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
def get_tickets(db: Session = Depends(get_db)):
    all_records = db.query(TicketInfo).all()
    return jsonable_encoder(all_records)

@router.post("/")
def create_ticket(ticket: ticket_model.TicketInfo, db: Session = Depends(get_db)):
    ticket = TicketInfo(**ticket.dict())
    db.add(ticket)
    db.commit()
    return {"message": "Ticket created"}

@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(TicketInfo).filter(TicketInfo.TICKET_ID == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(ticket)
    db.commit()
    return {"message": f"Ticket {ticket.TICKET_ID} deleted successfully"}


@router.put("/{ticket_id}")
def update_flight(ticket_id: int, updated_ticket: ticket_model.TicketInfoUpdate, db: Session = Depends(get_db)):
    ticket = db.query(TicketInfo).filter(TicketInfo.TICKET_ID == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    # TODO: improve this
    ticket.FLIGHT_ID = updated_ticket.FLIGHT_ID
    ticket.PROFILE_ID = updated_ticket.PROFILE_ID
    ticket.STATUS = updated_ticket.STATUS

    db.add(ticket)
    db.commit()
    return {"message": f"Ticket {ticket.TICKET_ID} updated successfully"}