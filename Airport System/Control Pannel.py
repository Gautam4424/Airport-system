import mysql.connector

connection=mysql.connector.connect(host='localhost',user='root',passwd='Gautam@4424',database='airport')
cur=connection.cursor()

print("Welcome to control pannel \n You can add the flight")
Entries_input=int(input("Press 1 to Show All The tables in your database :"))
if Entries_input==1:
    cur.execute("SHOW TABLES")
    a=1
    for i in cur:
        print(a,i)
        a+=1
    Table_Input=int(input("Enter the number of table which you have to modify"))
    if Table_Input==1:
        print("What You Want to do in your Table : \n1. Add Entries \n2.Delete Entries \n3. Reset Table")
        Choise_input=int(input("Enter your choise :"))
        if Choise_input==1:
            Loop_Entries = int(input("How many Entries You Want to add :"))
            for j in range(Loop_Entries):
                Flight_No=input("Enter the flight Number Here :")
                Date_Of_Departure=input("Enter the date of departure here(YYYY/MM/DD) :")
                Time =input("Enter the time (HH:MM) :")
                Type =input("Enter the type of the flight National/International :")
                Departure=input("Enter the dapature place of the flight :")
                Destination=input("Enter the Destination of the flight :")
                price=input("Enter the price")
                Confirmation=int(input("Enter 1 to add the entry in your database :"))
                if Confirmation==1:
                    try:
                        cur.execute(
                            "INSERT INTO Flights (Flight_No,Date_Of_Departure,Time,Type,Departure,Destination,Price) values('{}','{}','{}','{}','{}','{}','{}')".format(
                                Flight_No, Date_Of_Departure, Time, Type, Departure, Destination,price))
                        connection.commit()
                        print("Added successfully")

                    except Exception as e:
                        print("Table Not Updated")


        if Choise_input == 2:
            Time_Entry = int(input("How Many Entries you want to delete :"))
            for i in range(Time_Entry):
                Flight_No2 = input("Enter the Flight Number you want to delete :")
                comfirmation = int(input("press 1 to continue :"))
                if comfirmation == 1:
                    try:
                        cur.execute("DELETE  FROM FLIGHTS WHERE FLIGHT_NO='{}'".format(Flight_No2))
                        connection.commit()
                        print("Delete Successfully")
                    except Exception as e:
                        print("Flight Number Not Found ")
































"""create table Flights(
     Flight_No varchar(100),
     Date_Of_Departure varchar(100),
     Time varchar(100),
     Type varchar(100),
     Departure varchar(100),
     Destination varchar(100),
     price varchar(100));"""

""""> create table user(
    -> Name varchar(100),
    -> Phone_Number varchar(100),
    -> Gender varchar(100),
    -> Ticket_Number varchar(100));"""
