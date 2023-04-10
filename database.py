import config
import cx_Oracle
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine.url import URL

def create_engine_with_oracle_client():
    cx_Oracle.init_oracle_client(lib_dir=config.PATH_TO_ORACLE_CLIENT)

    url = URL.create(drivername='oracle+cx_oracle',
                    username="Maryam",
                    password="12345678",
                    host="localhost",
                    port="1521",
                    database="xe"
    )

    connection_str = f"oracle+cx_oracle://{config.USERNAME}:{config.PASSWORD}{config.HOST}:{config.PORT}/{config.DATABASE}"
    print(f"{connection_str}")
    engine = create_engine(url)
    return engine


engine = create_engine_with_oracle_client()
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class Flight(Base):
    __tablename__ = 'FLIGHT'

    FLIGHT_ID = Column(Integer, primary_key=True, nullable=False)
    AIRLINE_ID = Column(Integer, nullable=False)
    AIRLINE_NAME = Column(String(55), nullable=False)
    TO_LOCATION = Column(String(55), nullable=False)
    LOCAL_SEATS = Column(Integer)

class PassengerProfile(Base):
    __tablename__ = 'PASSENGER_PROFILE'

    PROFILE_ID = Column(Integer, primary_key=True)
    PASSWORD = Column(Integer, nullable=False)
    FIRST_NAME = Column(String(20), nullable=False)
    EMAIL_ADDRESS = Column(String(50))

class TicketInfo(Base):
    __tablename__ = 'TICKET_INFO'

    TICKET_ID = Column(Integer, primary_key=True)
    FLIGHT_ID = Column(Integer, ForeignKey('FLIGHT.FLIGHT_ID'), nullable=False)
    PROFILE_ID = Column(Integer, ForeignKey('PASSENGER_PROFILE.PROFILE_ID'), nullable=False)
    STATUS = Column(String(20), nullable=False)


# all_flights = session.query(Flight).all()
# for flight in all_flights:
#     print(flight.FLIGHT_ID)



# all_passangers = session.query(PassengerProfile).all()
# for passenger in all_passangers:
#     print(passenger.PROFILE_ID)


# all_tickets = session.query(TicketInfo).all()
# for ticket in all_tickets:
#     print(ticket.TICKET_ID)
