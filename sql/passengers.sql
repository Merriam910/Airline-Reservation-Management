CREATE TABLE PASSENGER_PROFILE
(
profile_ID number(10) NOT NULL,
password number(8) NOT NULL,
first_name varchar(20) NOT NULL,
email_address varchar2(50),
PRIMARY KEY (profile_ID)
);