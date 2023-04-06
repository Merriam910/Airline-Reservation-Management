CREATE TABLE Flight
(
flight_ID number(10) NOT NULL,
Airline_ID number(10) NOT NULL,
airline_name varchar2(55) NOT NULL,
from_location varchar2(55) NOT NULL,
to_location varchar2(55), 
local_seats number(10),
CONSTRAINT flight_pk PRIMARY KEY (flight_ID)
CONSTRAINT CHK_seats CHECK (local_seats>=0)
);