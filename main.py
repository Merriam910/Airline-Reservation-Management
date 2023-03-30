import cx_Oracle

PATH_TO_ORACLE_CLIENT = "C:\\oracle\\"
cx_Oracle.init_oracle_client(lib_dir=PATH_TO_ORACLE_CLIENT) 

USERNAME = "hr"
PASSWORD = "12345678@"
HOST = "localhost"
PORT = 1521
DATABASE = "xe"

CONNECTION_STRING = f"{USERNAME}/{PASSWORD}//{HOST}:{PORT}/{DATABASE}"

conn=cx_Oracle.connect(CONNECTION_STRING)
print("Orcale, is connected to ",conn.version, " version of database.")

cur=conn.cursor()

while True:
    print('welcome! to the program.')
    print()
    print('PRESS 1 to insert the data\n')
    print('PRESS 2 to display the data\n')
    print('PRESS 3 to delete the data\n')
    print('PRESS 4 to update the data\n')
    print('PRESS 5 to search the data\n')
    print()
    try:
        choice = int(input('Enter the choice '))

        if choice == 1:
            # insert
            username = input('Enter your name. ')
            phone = input('Enter your phone number. ')
            query = "insert into STUDENT_DETAILS(FIRST_NAME,LAST_NAME) values('{}','{}')".format(username, phone)
            # print(query)
            cur.execute(query)
            conn.commit()
            print("data",username,phone,"saved to db")
            input()
        elif choice == 2:
            # display data
            query = "select * from STUDENT_DETAILS"

            # print(query)
            cur.execute(query)
            print('---------------------------')
            postion=1
            for row in cur:
                print('Record no.',postion)
                srno=1
                print('|',srno,"FIRST_NAME : ", row[0],'|')
                print('|',srno+1,"LAST_NAME  : ", row[1],'|')
                postion=postion+1
                #print('***************************')
            print('---------------------------')
            input()
        elif choice == 3:
            # delete the data
            delete_RecordId=input('Enter the record id you want to delete.')
            query = "delete from STUDENT_DETAILS where LAST_NAME= '{}'".format(delete_RecordId)
            #print(query)
            cur.execute(query)
            conn.commit()
            print("data id", delete_RecordId, "deleted from db")
            input()
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
