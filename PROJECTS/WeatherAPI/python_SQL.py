# this file connects to mysql, revolves around exporting the data to mysql db;

import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
from extractData import fetchData


# username="root",
# password="root",
# host="localhost"
# database="weather_data"

def baseDatabseTableCreation():
    mydb = mysql.connector.connect(
        username="root",
        password="root",
        host="localhost"
    )

    if mydb:
        print("Database connection established")
        
    myCursor = mydb.cursor()
    myCursor.execute("show databases")
    for db in myCursor:
        print(db)

    myCursor.execute("use weather_database")
    print("Using weather_database now..")

    months_table = """create table Months (
                        Month_ID int primary key,
                        Month_Name varchar(30)
                        );"""

    myCursor.execute(months_table)
    print("Months Table created successfully.")

    attributes_table = """create table Attributes (
                        Attribute_ID int primary key,
                        Attribute_Name varchar(50)
                        );"""

    myCursor.execute(attributes_table)
    print("Attributes Table created successfully.")

    weather_data_table = """create table Weather_Data (
                            Record_ID int primary key,
                            Month_ID int,
                            Attribute_ID int,
                            Value float,
                            foreign key (Month_ID) references Months(Month_ID),
                            foreign key (Attribute_ID) references Attributes(Attribute_ID)
                        );"""

    myCursor.execute(weather_data_table)
    print("Weather Data Table created successfully.")


# importing a dataframe from here on using sqlalchemy
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
temperatures, humidity, sunrises, sunsets, sunshineDurations, daylightDurations, maxTemperatures, minTemperatures = fetchData()


data = pd.DataFrame({
    "Month": months,
    "Temperature": temperatures,
    "Humidity": humidity,
    "Sunrise_Times": sunrises,
    "Sunset_Times": sunsets,
    "Sunshine_Durations": sunshineDurations,
    "Daylight_Durations": daylightDurations,
    "Maximum_Temperatures": maxTemperatures,
    "Minimum_Temperatures": minTemperatures,
})


# connection engine creation here
# engine = create_engine(f"mysql+plmysql://{username}:{password}@{host}//{database}")

# data.to_sql(
#     name="weather"
# )


def insertValues():
    mydb = mysql.connector.connect(
        username="root",
        password="root",
        host="localhost",
        database="weather_database"
    )

    if mydb:
        print("Database connection established")
    
    myCursor = mydb.cursor()

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    attributes = ["Temperatures", "Humidity", "Sunrise_Times", "Sunset_Times", "Sunshine_Hours", "Daylight_Hours", "Max_Temp", "Min_Temp"]

    # inserting into month table
    for i,month in enumerate(months):
        myCursor.execute("INSERT INTO Months VALUES (%s, %s)", (i+1, month))

    # inserting into attribute table
    for i,attr in enumerate(attributes):
        myCursor.execute("INSERT INTO Attributes VALUES (%s, %s)", (i+1, attr))

    # inserting into weather data tablee


def monthTableValues():

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    monthTable = pd.DataFrame({
        "Month_ID":[1,2,3,4,5,6,7,8,9,10,11,12],
        "Month_Name": months 
    })
    
#connection engine creation here
    username = "root"
    password = "root"
    host = "localhost"
    database = "weather_database"
    # engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}//{database}")
    engine = create_engine("mysql+pymysql://root:root@localhost/weather_database")


    monthTable.to_sql(
        name = "months",
        con = engine,
        if_exists = "replace",
        index = False
    )
monthTableValues()

 


    

    

    


    







