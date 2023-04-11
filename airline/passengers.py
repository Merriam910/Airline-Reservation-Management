from airline.driver import connect
from prettytable import from_db_cursor
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
        num_rows_deleted = cur.rowcount #checks how many rows are effected
        conn.commit()

        if num_rows_deleted > 0:
            print(f"Deleted profile {profile_id}")
            return
        print("NO SUCH DATA FOUND")
        return 
    
     
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
        num_rows_updated = cur.rowcount #checks how many rows are effected
        conn.commit()

        if num_rows_updated > 0:
            print(f"UPDATED Passenger {profile_id}")
            return  
        print("NO SUCH DATA FOUND")
        return 