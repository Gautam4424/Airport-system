import mysql.connector

connection=mysql.connector.connect(host='localhost',user='root',passwd="Gautam@4424",database="airport")
cur=connection.cursor()

print("Welcome to aasspp Airport")

print("Press 1 for the Registration ")
print("Press 2 for getting the information About the pressenger")
print("Press 3 for Search for the flights")
user_input=int(input("Enter your choice"))

if user_input==1:
    import Registration
    Registration.getting_information()
elif user_input==2:
    import pessengerInfo
    pessengerInfo.Pessenger_info()
elif user_input==3:
    import Searchflight
    Searchflight.Search()
