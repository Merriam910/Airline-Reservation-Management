from airline.driver import connect
from prettytable import from_db_cursor
def create_flight():
    columns_list = ["FLIGHT_ID", "AIRLINE_ID", "AIRLINE_NAME", "TO_LOCATION", "LOCAL_SEATS"]
    values = []
    number_columns = ["LOCAL_SEATS"]  
    for column in columns_list:
        value = input(f"Enter your {column}: ")
        if value in number_columns: # if LOCAL_SEATS in ["LOCAL_SEATS"] , gives true
            value = int(value) # casting string to int
        values.append(value) # append is for arrays. it means add to list

    columns_to_insert = ",".join(columns_list) # changes an array to a string and seperates them with a ',' ["a", "b", "c"] --> "a,b,c"
    
    with connect() as conn: # Context manager. after with it closes the database connection. We do this to manage our resources
        cur=conn.cursor()
        query = f"""INSERT INTO FLIGHT({columns_to_insert}) values{tuple(values)}"""  # tuples(values) means casting our values(which is list) to tuples. [1,2,3] -> (1,2,3)
        cur.execute(query)
        conn.commit()
    print(f"Flight created!",style="cong")

def get_all_flights():
    with connect() as conn:
        query = "SELECT * FROM FLIGHT"
        cur=conn.cursor()
        cur.execute(query)
        flights_table = from_db_cursor(cur) # function from prettytable python package which uses the database cursor and makes a table for printing to console
        print(flights_table)

def delete_flight():
    flight_id=input('Enter the flight id you want to delete: ')
    flight_id.lower()
    if flight_id.strip() == '': # check if there no user input. strip removes white spaces "  HELLO WORLD  " --> "HELLO WORLD"
        print("Please give an valid flight_id!")
        return # stop the code, don't render the stuff below because user input. return nothing
    with connect() as conn:
        cur=conn.cursor()
        query = f"DELETE FROM FLIGHT WHERE flight_id= '{flight_id}'"
        cur.execute(query)
        conn.commit()
    print(f"Deleted flight {flight_id}!")
    
def update_flight():
    flight_id=input('Enter the flight id you want to update: ')
    if flight_id.strip() == '':
        print("Please give an valid flight_id!")
        return
    columns=("AIRLINE_ID", "AIRLINE_NAME", "TO_LOCATION", "LOCAL_SEATS")
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
        query = f"UPDATE FLIGHT SET {update_string} WHERE flight_id= '{flight_id}'" # update the record for the condition (WHERE) in this case flight_id="xxx" 
        cur.execute(query)
        conn.commit()
    print(f"Updated flight {flight_id}!")