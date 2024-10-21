import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def fetchData():

    url = "https://archive-api.open-meteo.com/v1/archive?latitude=28.6519&longitude=77.2315&start_date=2023-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,daylight_duration,sunshine_duration&timezone=Asia%2FBangkok"

    startTimeWithHours = [
        "2023-01-01T00:00",  # jan
        "2023-02-01T00:00",  # feb
        "2023-03-01T00:00",  # march
        "2023-04-01T00:00",  # april
        "2023-05-01T00:00",  # may
        "2023-06-01T00:00",  # june
        "2023-07-01T00:00",  # july
        "2023-08-01T00:00",  # aug
        "2023-09-01T00:00",  # sept
        "2023-10-01T00:00",  # oct
        "2023-11-01T00:00",  # nov
        "2023-12-01T00:00"   # dec
    ]

    endTimeWithHours = [
        "2023-01-31T23:00",  # jan
        "2023-02-28T23:00",  # feb
        "2023-03-31T23:00",  # march
        "2023-04-30T23:00",  # april
        "2023-05-31T23:00",  # may
        "2023-06-30T23:00",  # june
        "2023-07-31T23:00",  # july
        "2023-08-31T23:00",  # aug
        "2023-09-30T23:00",  # sept
        "2023-10-31T23:00",  # oct
        "2023-11-30T23:00",  # nov
        "2023-12-31T23:00"   # decS
    ]

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
    
    temperatures = []
    humidity = []
    sunrises = []
    sunsets = []
    sunshineDurations = []
    daylightDurations = []
    maxTemperatures = []
    minTemperatures = []
 
    
    response = requests.get(url).json()
    hourly = pd.DataFrame(response["hourly"])
    daily = pd.DataFrame(response["daily"])

    for i in range(len(endTime)):

        tempLogic = (hourly["time"] >= startTimeWithHours[i]) & (hourly["time"] <= endTimeWithHours[i])
        tempData = hourly[tempLogic][["temperature_2m","relative_humidity_2m"]]
        stats = tempData.describe().round(3)
        temp = stats.loc["mean", "temperature_2m"]
        humid = stats.loc["mean", "relative_humidity_2m"]
        temperatures.append(temp)
        humidity.append(humid)


        logic = (daily["time"] >= startTime[i]) & (daily["time"] <= endTime[i])
        minMaxTemps = daily[logic][["temperature_2m_max", "temperature_2m_min"]]
        stats = minMaxTemps.describe()
        maxTemp = stats.loc["max"]["temperature_2m_max"]
        minTemp = stats.loc["min"]["temperature_2m_min"]
        maxTemperatures.append(maxTemp)
        minTemperatures.append(minTemp)


        sunshineLogic = (daily["time"] >= startTime[i]) & (daily["time"] <= endTime[i])
        durations = daily[sunshineLogic][["daylight_duration","sunshine_duration"]]
        stats = durations.describe().round(3)
        daylight = ((stats.loc["mean", "daylight_duration"])//60)//60
        sunshine = ((stats.loc["mean", "sunshine_duration"])//60)//60
        sunshineDurations.append(sunshine)
        daylightDurations.append(daylight)


        monthLogic = (daily["time"] >= startTime[i]) & (daily["time"] <= endTime[i])
        data = daily[monthLogic][["sunrise","sunset"]]
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
    

    return temperatures, humidity, sunrises, sunsets, sunshineDurations, daylightDurations, maxTemperatures, minTemperatures






        

    
    
