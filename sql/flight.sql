CREATE TABLE Flight
(
flight_ID number(10) NOT NULL,
Airline_ID number(10) NOT NULL,
airline_name varchar2(55) NOT NULL,
from_location varchar2(55) NOT NULL,
to-location varchar2(55), 
local_seats number(10),
PRIMARY KEY (flight_ID)
); 