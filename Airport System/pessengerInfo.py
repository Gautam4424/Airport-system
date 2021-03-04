import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', passwd='Gautam@4424', database='airport')
cur = connection.cursor()


def Pessenger_info():
    Ticket_Num = input("Enter the ticket Number of the pessenger")
    cur.execute("SELECT * FROM USER WHERE Ticket_Number='{}'".format(Ticket_Num))
    output = cur.fetchall()
    if output != []:
        print(output)
    else:
        print("Please enter valid Ticket Number")
