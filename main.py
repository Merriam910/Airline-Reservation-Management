import cx_Oracle
import config

cx_Oracle.init_oracle_client(lib_dir=config.PATH_TO_ORACLE_CLIENT)
conn=cx_Oracle.connect(config.CONNECTION_STRING)
print("Orcale, is connected to ",conn.version, " version of database.")

cur=conn.cursor()

def insert_data(username, last_name):
    query = f"""INSERT INTO STUDENT_DETAILS(FIRST_NAME,LASTNAME) values('{username}','{last_name}')"""
    cur.execute(query)
    conn.commit()

def show_data():
    query = "select * from STUDENT_DETAILS"
    cur.execute(query)
    if not cur:
        print("No records found")
        return
    for idx, row in enumerate(cur):
        first_name = row[0]
        last_name = row[1]
        print(f"{idx}| {first_name} {last_name}")

def delete_user(user_id):
    query = f"delete from STUDENT_DETAILS where LASTNAME= '{user_id}'"
    cur.execute(query)
    conn.commit()

print("""
Welcome to the Airline Database Manager
Options:
- 1 | insert data
- 2 | display data
- 3 | delete data
- 4 | update data
- 5 | search data
""")

while True:

    try:
        choice = int(input('Enter the choice '))

        if choice == 1:
            # insert
            username = input('Enter your name: ')
            last_name = input('Enter your last name: ')
            insert_data(username=username, last_name=last_name)
            print(f"data to database!")

        elif choice == 2:
            show_data()

        elif choice == 3:
            # delete the data
            delete_RecordId=input('Enter the record id you want to delete: ')
            delete_user(user_id=delete_RecordId)

        elif choice == 4:
            # update
            pass
        elif choice == 5:
            # search
            status='false'
            search_RecordId = input('Enter the record id you want to search.')
            query = "select LAST_NAME from STUDENT_DETAILS"
            cur.execute(query)
            for row in cur:
                if search_RecordId==row[0]:
                    status='true'
            print('---------------------------')
            if status=='true':
                query = "select * from STUDENT_DETAILS where LAST_NAME= '{}'".format(
                    search_RecordId)
                cur.execute(query)
                postion = 1
                for row in cur:
                    print('Record no.', postion)
                    srno = 1
                    print('|', srno, "FIRST_NAME : ", row[0], '|')
                    print('|', srno + 1, "LAST_NAME  : ", row[1], '|')
                    postion = postion + 1
                    # print('***************************')
                print('---------------------------')
                input()
            else:
                print('No, record found for', search_RecordId)
                print('---------------------------')
                input()
        else:
            print('invalid input! try again.')
            print()
    except Exception as e:
        print(e)
        print('invalid data')
