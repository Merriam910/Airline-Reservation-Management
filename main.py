import cx_Oracle
import config
import sys
from prettytable import from_db_cursor
cx_Oracle.init_oracle_client(lib_dir=config.PATH_TO_ORACLE_CLIENT)

def connect():
    return cx_Oracle.connect(config.CONNECTION_STRING)
# print("Orcale, is connected to ",conn.version, " version of database.")



def create_flight():
    columns = ["FLIGHT_ID", "AIRLINE_ID", "AIRLINE_NAME", "TO_LOCATION", "LOCAL_SEATS"]
    values = []
    for column in columns:
        value = input(f"Enter your {column}: ")
        if value ==  "LOCAL_SEATS":
            value = int(value)
        values.append(value)

    columns_to_insert = ",".join(columns)
    
    with connect() as conn:
        cur=conn.cursor()
        query = f"""INSERT INTO FLIGHT({columns_to_insert}) values{tuple(values)}""" 
        cur.execute(query)
        conn.commit()
    print(f"Flight created!")

def get_all_flights():
    """Returns all flights as a list"""
    with connect() as conn:
        query = "SELECT * FROM FLIGHT"
        cur=conn.cursor()
        cur.execute(query)
        flights_table = from_db_cursor(cur)
        print(flights_table)

def delete_flight():
    flight_id=input('Enter the flight id you want to delete: ')
    if flight_id.strip() == '':
        print("Please give an valid flight_id!")
        return
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
            updates.append(f"{column} = '{value}'")

    if not updates:
        print("Nothing to add")
        return

    update_string = (',').join(updates)

    with connect() as conn:
        cur=conn.cursor()
        query = f"UPDATE FLIGHT SET {update_string} WHERE flight_id= '{flight_id}'"
        print(query)
        cur.execute(query)
        conn.commit()
    print(f"Deleted flight {flight_id}!")

def main():
    OPTIONS = {
        "1": {"logic": create_flight , "description": "1 |\tCreate a new flight"},
        "2": {"logic": get_all_flights , "description": "2 |\tShow all flights"},
        "3": {"logic": delete_flight , "description": "3 |\tRemove a flight"},
        "4": {"logic": update_flight , "description": "4 |\tUpdate a flight"},
        "5": {"logic": sys.exit, "description": "5 |\tClose the application"}
    }

    while True:
        for key, value in OPTIONS.items():
            print(value['description'])

        
        choice = input('Enter the choice: ')
        if choice in OPTIONS:
            OPTIONS[choice]['logic']()
            continue

        print("Please select an valid option")


if __name__ == "__main__":
    main()


