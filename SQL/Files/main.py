import mysql.connector

dbcon = mysql.connector.connect(
                        username="root",   
                        password="root", 
                        host="localhost")
print(dbcon)

cur = dbcon.cursor()
cur.execute("create database sample")
dbcon.commit()
dbcon.close()
print("database created successfully")
