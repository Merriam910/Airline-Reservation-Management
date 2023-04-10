from airline.driver import connect
from prettytable import from_db_cursor
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
        num_rows_deleted = cur.rowcount #checks how many rows are effected
        conn.commit()

        if num_rows_deleted > 0:
            print(f"Deleted Ticket {ticket_id}")
        
        print("NO SUCH DATA FOUND")
        return 
    
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