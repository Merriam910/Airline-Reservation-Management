CREATE TABLE Flight
(
flight_ID number(10) NOT NULL,
Airline_ID number(10) NOT NULL,
airline_name varchar2(55) NOT NULL,
from_location varchar2(55) NOT NULL,
to_location varchar2(55), 
local_seats number(10),
CONSTRAINT flight_pk PRIMARY KEY (flight_ID)
CONSTRAINT CHK_seats CHECK (local_seats>=0 AND local_seats<2300)
);
#CHECKS
ALTER TABLE PASSENGER_PROFILE
add CONSTRAINT chk_FIRST_NAME CHECK(FIRST_NAME not like '[0-9]')
ALTER TABLE PASSENGER_PROFILE
add CONSTRAINT chek_FIRST_NAME CHECK(FIRST_NAME  not like '%[!@#%^&*_+-]%')
ALTER TABLE FLIGHT
ADD CONSTRAINT chk_FLIGHT_ID CHECK(FLIGHT_ID  >0 and FLIGHT_ID <99999)