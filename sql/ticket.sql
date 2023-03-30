CREATE TABLE TICKET_INFO
(
flight_ID number(10) NOT NULL,
ticket_ID number(10) NOT NULL,
profile_ID number(20) NOT NULL,
status varchar2(50) NOT NULL,
PRIMARY KEY (ticket_ID)
);