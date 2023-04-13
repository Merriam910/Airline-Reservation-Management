CREATE TABLE TICKET_INFO
(ticket_ID number(10) NOT NULL,
flight_ID number(10) NOT NULL,
profile_ID number(10) NOT NULL,
status varchar(20) NOT NULL,
CONSTRAINT ticket_pk PRIMARY KEY (ticket_ID),
);
ALTER TABLE Ticket_info
ADD CONSTRAINT fk_profile_id
FOREIGN KEY (profile_id) REFERENCES passenger_profile (profile_id)
ON DELETE CASCADE;
ALTER TABLE Ticket_info
ADD CONSTRAINT fk_flight_id
FOREIGN KEY (flight_id) REFERENCES flight (flight_id)
ON DELETE CASCADE;