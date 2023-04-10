import cx_Oracle
import config
import sys
import login
from prettytable import from_db_cursor
from tkinter import *
from airline import flights

def connect():
    return cx_Oracle.connect(config.CONNECTION_STRING)


def create_passenger():
    columns_list = ["PROFILE_ID", "PASSWORD", "FIRST_NAME", "EMAIL_ADDRESS"]
    values = []
    number_columns = ["PASSWORD"]  
    for column in columns_list:
        value = input(f"Enter your {column}: ")
        if value in number_columns: # if LOCAL_SEATS in ["LOCAL_SEATS"] , gives true
            value = int(value) # casting string to int
        values.append(value) # append is for arrays. it means add to list

    columns_to_insert = ",".join(columns_list) # changes an array to a string and seperates them with a ',' ["a", "b", "c"] --> "a,b,c"
    
    with connect() as conn: # Context manager. after with it closes the database connection. We do this to manage our resources
        cur=conn.cursor()
        query = f"""INSERT INTO PASSENGER_PROFILE({columns_to_insert}) values{tuple(values)}"""  # tuples(values) means casting our values(which is list) to tuples. [1,2,3] -> (1,2,3)
        cur.execute(query)
        conn.commit()
    print(f"Passenger Added!")
def get_all_passengers():
 with connect() as conn:
        query = "SELECT * FROM PASSENGER_PROFILE"
        cur=conn.cursor()
        cur.execute(query)
        passenger_table = from_db_cursor(cur) # function from prettytable python package which uses the database cursor and makes a table for printing to console
        print(passenger_table)
def delete_passenger():
    profile_id=input('Enter the profile id you want to delete: ')
    if profile_id.strip() == '': # check if there no user input. strip removes white spaces "  HELLO WORLD  " --> "HELLO WORLD"
        print("Please give an valid profile_id!")
        return # stop the code, don't render the stuff below because user input. return nothing
    with connect() as conn:
        cur=conn.cursor()
        query = f"DELETE FROM PASSENGER_PROFILE WHERE profile_id= '{profile_id}'"
        cur.execute(query)
        conn.commit()
    print(f"Deleted profile {profile_id}!")  
def update_passenger():
    profile_id=input('Enter the profile id you want to update: ')
    if profile_id.strip() == '':
        print("Please give an valid profile_id!")
        return
    columns=("PROFILE_ID", "PASSWORD", "FIRST_NAME", "EMAIL_ADDRESS")
    updates = []
    for column in columns:
        value = input(f'The new value for {column}. Leave empty to skip: ')
        if not value.strip() == '':
            updates.append(f"{column} = '{value}'")  # AIRLINE_ID= '1' --> adds to list ["AIRLINE_ID= '1'",  "TO_LOCATION= 'A'"]

    if not updates: # when there is nothing to the list stop with this function and return nothing
        print("Nothing to add")
        return

    update_string = (',').join(updates) # ["AIRLINE_ID= '1'",  "TO_LOCATION= 'A'"] --> "AIRLINE_ID= '1',TO_LOCATION= 'A'"  

    with connect() as conn:
        cur=conn.cursor()
        query = f"UPDATE PASSENGER_PROFILE SET {update_string} WHERE profile_id= '{profile_id}'" # update the record for the condition (WHERE) in this case flight_id="xxx" 
        cur.execute(query)
        conn.commit()
    print(f"Updated passenger {profile_id}!")  
def create_ticket():
    columns_list = ["TICKET_ID","FLIGHT_ID","PROFILE_ID","STATUS"]
    values = []
    number_columns = ["TICKET_ID"]  
    for column in columns_list:
        value = input(f"Enter your {column}: ")
        if value in number_columns: # if LOCAL_SEATS in ["LOCAL_SEATS"] , gives true
            value = int(value) # casting string to int
        values.append(value) # append is for arrays. it means add to list

    columns_to_insert = ",".join(columns_list) # changes an array to a string and seperates them with a ',' ["a", "b", "c"] --> "a,b,c"
    
    with connect() as conn: # Context manager. after with it closes the database connection. We do this to manage our resources
        cur=conn.cursor()
        query = f"""INSERT INTO TICKET_INFO({columns_to_insert}) values{tuple(values)}"""  # tuples(values) means casting our values(which is list) to tuples. [1,2,3] -> (1,2,3)
        cur.execute(query)
        conn.commit()
    print(f"Ticket Added!") 
def get_all_tickets():
 with connect() as conn:
        query = "SELECT * FROM TICKET_INFO"
        cur=conn.cursor()
        cur.execute(query)
        ticket_table = from_db_cursor(cur) # function from prettytable python package which uses the database cursor and makes a table for printing to console
        print(ticket_table)
def delete_tickets():
    ticket_id=input('Enter the ticket id you want to delete: ')
    if ticket_id.strip() == '': # check if there no user input. strip removes white spaces "  HELLO WORLD  " --> "HELLO WORLD"
        print("Please give an valid ticket_id!")
        return # stop the code, don't render the stuff below because user input. return nothing
    with connect() as conn:
        cur=conn.cursor()
        query = f"DELETE FROM TICKET_INFO WHERE ticket_id= '{ticket_id}'"
        cur.execute(query)
        conn.commit()
    print(f"Deleted ticket {ticket_id}!") 
def update_tickets():
    ticket_id=input('Enter the ticket id you want to update: ')
    if ticket_id.strip() == '':
        print("Please give an valid ticket_id!")
        return
    columns=("TICKET_ID","FLIGHT_ID","PROFILE_ID", "STATUS")
    updates = []
    for column in columns:
        value = input(f'The new value for {column}. Leave empty to skip: ')
        if not value.strip() == '':
            updates.append(f"{column} = '{value}'")  # AIRLINE_ID= '1' --> adds to list ["AIRLINE_ID= '1'",  "TO_LOCATION= 'A'"]

    if not updates: # when there is nothing to the list stop with this function and return nothing
        print("Nothing to add")
        return

    update_string = (',').join(updates) # ["AIRLINE_ID= '1'",  "TO_LOCATION= 'A'"] --> "AIRLINE_ID= '1',TO_LOCATION= 'A'"  

    with connect() as conn:
        cur=conn.cursor()
        query = f"UPDATE TICKET_INFO SET {update_string} WHERE ticket_id= '{ticket_id}'" # update the record for the condition (WHERE) in this case flight_id="xxx" 
        cur.execute(query)
        conn.commit()
    print(f"Updated Ticket {ticket_id}!") 
def ticket_menu():
     OPTIONS={ "1": {"logic": create_ticket , "description": "1 |\tCreate a new ticket"},
        "2": {"logic": get_all_tickets , "description": "2 |\tShow all tickets"},
        "3": {"logic": delete_tickets , "description": "3 |\tRemove a ticket"},
        "4": {"logic": update_tickets , "description": "4 |\tUpdate a ticket"},
        "5": {"logic": passenger_menu, "description": "5 |\tGo Back to passengers menu"},
        "6": {"logic": main, "description": "6 |\tGo Back To flights Menu"}}
     while True:
        for key, value in OPTIONS.items(): # items makes you loop over the dictionary as key, value (first iteration): "1", {"logic": create_flight , "description": "1 |\tCreate a new flight"},
            print(value['description'])

        
        choice_P = input('Enter the choice: ')
        if choice_P in OPTIONS:
            OPTIONS[choice_P]['logic']()
            continue

        print("Please select an valid option")
def passenger_menu():
     OPTIONS={ "1": {"logic": create_passenger , "description": "1 |\tCreate a new passenger"},
        "2": {"logic": get_all_passengers , "description": "2 |\tShow all passengers"},
        "3": {"logic": delete_passenger , "description": "3 |\tRemove a passenger"},
        "4": {"logic": update_passenger , "description": "4 |\tUpdate a passenger"},
        "5": {"logic": ticket_menu, "description": "5 |\tView options for Tickets"},
        "6": {"logic": main, "description": "6 |\tGo Back To flights Menu"}}
     while True:
        for key, value in OPTIONS.items(): # items makes you loop over the dictionary as key, value (first iteration): "1", {"logic": create_flight , "description": "1 |\tCreate a new flight"},
            print(value['description'])

        
        choice_P = input('Enter the choice: ')
        if choice_P in OPTIONS:
            OPTIONS[choice_P]['logic']()
            continue

        print("Please select an valid option")
def main():
    OPTIONS = {
        "1": {"logic": flights.create_flight , "description": "1 |\tCreate a new flight"},
        "2": {"logic": flights.get_all_flights , "description": "2 |\tShow all flights"},
        "3": {"logic": flights.delete_flight , "description": "3 |\tRemove a flight"},
        "4": {"logic": flights.update_flight , "description": "4 |\tUpdate a flight"},
        "5": {"logic": passenger_menu, "description": "5 |\tView options for Passenger"},
        "6": {"logic": ticket_menu, "description": "6 |\tView options for Ticket"},
        "7": {"logic": sys.exit, "description": "7 |\tClose the application"}
    } # dictionary in a dictionary. so for key 1 it stores a dictionary, which contains the key logic and description

    while True:
        for key, value in OPTIONS.items(): # items makes you loop over the dictionary as key, value (first iteration): "1", {"logic": create_flight , "description": "1 |\tCreate a new flight"},
            print(value['description'])

        
        choice = input('Enter the choice: ')
        if choice in OPTIONS:
            OPTIONS[choice]['logic']()
            continue

        print("Please select an valid option")


if __name__ == "__main__":
    main()
