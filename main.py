import cx_Oracle
import config
import sys
import login

from prettytable import from_db_cursor
from tkinter import *
from airline import flights,tickets,passengers

def connect():
    return cx_Oracle.connect(config.CONNECTION_STRING)

def ticket_menu():
     print("\033[92m\033[1m\033[4m\n   ----AIRLINE RESERVATION MANAGEMENT SYSTEM----\n")
     OPTIONS={
         "1": {
          "logic": tickets.create_ticket , "description": "1 |\tCreate a new ticket"},
        "2": {"logic": tickets.get_all_tickets , "description": "2 |\tShow all tickets"},
        "3": {"logic": tickets.delete_tickets , "description": "3 |\tRemove a ticket"},
        "4": {"logic": tickets.update_tickets , "description": "4 |\tUpdate a ticket"},
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
     print("\033[96m\033[1m\033[4m\n   ----AIRLINE RESERVATION MANAGEMENT SYSTEM----\n")
     OPTIONS={ "1": {"logic": passengers.create_passenger , "description": "1 |\tCreate a new passenger"},
        "2": {"logic": passengers.get_all_passengers , "description": "2 |\tShow all passengers"},
        "3": {"logic": passengers.delete_passenger , "description": "3 |\tRemove a passenger"},
        "4": {"logic": passengers.update_passenger , "description": "4 |\tUpdate a passenger"},
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
    print("\033[95m\033[1m\033[4m\n   ----AIRLINE RESERVATION MANAGEMENT SYSTEM----\n")

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
