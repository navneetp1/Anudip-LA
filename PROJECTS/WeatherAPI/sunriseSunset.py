from datetime import datetime, timedelta
import requests
import pandas as pd

# times = []

# date = "2023-01-01T08:43"
# date2 = "2023-01-01T09:43"
# t = date.split("T")[1]
# t2 = date2.split("T")[1]
# dateObject = datetime.strptime(t,"%H:%M")
# dateObject2 = datetime.strptime(t2,"%H:%M")
# print(type(dateObject))
# times.append(dateObject)
# times.append(dateObject2)
# print(times)

# def time_to_float(dt):
#     return dt.hour + dt.minute / 60

# floatTime = [round(time_to_float(time),2) for time in times]
# print(floatTime)


def sunriseAndSunsetDelhi():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=28.6519&longitude=77.2315&start_date=2023-01-01&end_date=2023-12-31&daily=sunrise,sunset&timezone=Asia%2FBangkok"

    response = requests.get(url).json()
    df = pd.DataFrame(response["daily"])
    
    sunrises = []
    sunsets = []

    startTime = [
        "2023-01-01",  # jan
        "2023-02-01",  # feb
        "2023-03-01",  # march
        "2023-04-01",  # april
        "2023-05-01",  # may
        "2023-06-01",  # june
        "2023-07-01",  # july
        "2023-08-01",  # aug
        "2023-09-01",  # sept
        "2023-10-01",  # oct
        "2023-11-01",  # nov
        "2023-12-01"   # dec
    ]

    endTime = [
        "2023-01-31",  # jan
        "2023-02-28",  # feb
        "2023-03-31",  # march
        "2023-04-30",  # april
        "2023-05-31",  # may
        "2023-06-30",  # june
        "2023-07-31",  # july
        "2023-08-31",  # aug
        "2023-09-30",  # sept
        "2023-10-31",  # oct
        "2023-11-30",  # nov
        "2023-12-31"   # decS
    ]

    for i in range(len(endTime)):
        monthLogic = (df["time"] >= startTime[i]) & (df["time"] <= endTime[i])
        data = df[monthLogic][["sunrise","sunset"]]
        sunriseTimes = pd.to_datetime(data["sunrise"]).dt.time
        sunsetTimes = pd.to_datetime(data["sunset"]).dt.time

        # converting to seconds
        sunrise_seconds = sunriseTimes.apply(lambda x: x.hour * 3600 + x.minute*60 + x.second)
        sunset_seconds = sunsetTimes.apply(lambda x: x.hour * 3600 + x.minute*60 + x.second)

        #mean
        avgSunrise = sunrise_seconds.mean()
        avgSunset = sunset_seconds.mean()

        # converting to time object
        avgSunriseTimdelta = timedelta(seconds=avgSunrise)
        avgSunsetTimedelta = timedelta(seconds=avgSunset)

        # adding with base time
        basetime = datetime(1970,1,1)
        avgSunriseTime = basetime + avgSunriseTimdelta
        avgSunsetTime = basetime + avgSunsetTimedelta

        #remove seconds and microseconds
        avgSunriseTime = avgSunriseTime.time().replace(microsecond=0, second=0)
        avgSunsetTime = avgSunsetTime.time().replace(microsecond=0, second=0)

        sunrises.append(avgSunriseTime)
        sunsets.append(avgSunsetTime)

    return sunrises, sunsets

def sunriseAndSunsetChennai():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=13.0878&longitude=80.2785&start_date=2023-01-01&end_date=2023-12-31&daily=sunrise,sunset&timezone=Asia%2FBangkok"

    response = requests.get(url).json()
    df = pd.DataFrame(response["daily"])
    
    sunrises = []
    sunsets = []

    startTime = [
        "2023-01-01",  # jan
        "2023-02-01",  # feb
        "2023-03-01",  # march
        "2023-04-01",  # april
        "2023-05-01",  # may
        "2023-06-01",  # june
        "2023-07-01",  # july
        "2023-08-01",  # aug
        "2023-09-01",  # sept
        "2023-10-01",  # oct
        "2023-11-01",  # nov
        "2023-12-01"   # dec
    ]

    endTime = [
        "2023-01-31",  # jan
        "2023-02-28",  # feb
        "2023-03-31",  # march
        "2023-04-30",  # april
        "2023-05-31",  # may
        "2023-06-30",  # june
        "2023-07-31",  # july
        "2023-08-31",  # aug
        "2023-09-30",  # sept
        "2023-10-31",  # oct
        "2023-11-30",  # nov
        "2023-12-31"   # decS
    ]

    for i in range(len(endTime)):
        monthLogic = (df["time"] >= startTime[i]) & (df["time"] <= endTime[i])
        data = df[monthLogic][["sunrise","sunset"]]
        sunriseTimes = pd.to_datetime(data["sunrise"]).dt.time
        sunsetTimes = pd.to_datetime(data["sunset"]).dt.time

        # converting to seconds
        sunrise_seconds = sunriseTimes.apply(lambda x: x.hour * 3600 + x.minute*60 + x.second)
        sunset_seconds = sunsetTimes.apply(lambda x: x.hour * 3600 + x.minute*60 + x.second)

        #mean
        avgSunrise = sunrise_seconds.mean()
        avgSunset = sunset_seconds.mean()

        # converting to time object
        avgSunriseTimdelta = timedelta(seconds=avgSunrise)
        avgSunsetTimedelta = timedelta(seconds=avgSunset)

        # adding with base time
        basetime = datetime(1970,1,1)
        avgSunriseTime = basetime + avgSunriseTimdelta
        avgSunsetTime = basetime + avgSunsetTimedelta

        #remove seconds and microseconds
        avgSunriseTime = avgSunriseTime.time().replace(microsecond=0, second=0)
        avgSunsetTime = avgSunsetTime.time().replace(microsecond=0, second=0)

        sunrises.append(avgSunriseTime)
        sunsets.append(avgSunsetTime)

    return sunrises, sunsets






# def demo():
#     import matplotlib.pyplot as plt
#     import numpy as np

#     # Example data: average sunrise and sunset times for each month (in hours)
#     months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#     sunrise = [7.0, 6.5, 6.0, 5.5, 5.0, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 7.5]  # Example sunrise times
#     sunset = [17.0, 17.5, 18.0, 19.0, 20.0, 20.5, 20.5, 20.0, 19.0, 18.0, 17.5, 17.0]  # Example sunset times

#     # Create the figure and axis
#     plt.figure(figsize=(10, 6))

#     # Plot sunrise and sunset data
#     plt.plot(months, sunrise, label="Sunrise", color='orange', marker='o')
#     plt.plot(months, sunset, label="Sunset", color='blue', marker='o')

#     # Fill between sunrise and sunset to show daylight hours
#     plt.fill_between(months, sunrise, sunset, color='skyblue', alpha=0.3)

#     # Adding labels and title
#     plt.xlabel('Month')
#     plt.ylabel('Time of Day (24-hour format)')
#     plt.title('Average Sunrise and Sunset Times for Each Month')
#     plt.legend()

# # Display the plot
#     plt.show()
