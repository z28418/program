#===================================================================================================================
#this is the file for handling databases aspect
#last checked 30/07/22
#==================================================================================================================
import mysql.connector

#create database thing when its up
#open = mysql.connector.connect(#user = username , password = password,
#host = hostip, database = databasename )

db_name = "appointments"
def create_db_tables():
    TABLES = {}
    TABLES["appointments"] = (
        "CREATE TABLE APPOINTMENTS("
        "Booking_NO int(5) NOT NULL AUTO_INCREMENT,"
        "first_name str(10) NOT NULL, "
        "last_name str(20) NOT NULL,"
        "date date NOT NULL"


    )


