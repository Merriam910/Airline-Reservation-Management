CREATE TABLE TICKET_INFO
(ticket_ID number(10) NOT NULL,
flight_ID number(10) NOT NULL,
profile_ID number(10) NOT NULL,
status varchar(20) NOT NULL,
CONSTRAINT ticket_pk PRIMARY KEY (ticket_ID),
CONSTRAINT fk_flight_ID  FOREIGN KEY (flight_ID) REFERENCES Flight(flight_ID),
CONSTRAINT fk_profile_ID  FOREIGN KEY (profile_ID) REFERENCES Passenger_profile(profile_ID)
);