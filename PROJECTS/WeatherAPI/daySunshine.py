# daylight and sunshine durations in delhi and chennai

import requests
import pandas as pd
from EDA import checkData

# delhi
def daylightAndSunshineDurationsDelhi():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=28.6519&longitude=77.2315&start_date=2023-01-01&end_date=2023-12-31&daily=daylight_duration,sunshine_duration&timezone=Asia%2FBangkok"

    response = requests.get(url).json()
    df = pd.DataFrame(response["daily"])
    checkData(df)



    avgSunshine = []
    avgDaylight = []

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
        monthData = df[monthLogic][["daylight_duration","sunshine_duration"]]

        stats = monthData.describe().round(3)
        daylight = ((stats.loc["mean", "daylight_duration"])//60)//60
        sunshine = ((stats.loc["mean", "sunshine_duration"])//60)//60
        
        avgSunshine.append(sunshine)
        avgDaylight.append(daylight)

    return avgSunshine, avgDaylight
        

# chennai api
def daylightAndSunshineDurationsChennai():
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=13.0878&longitude=80.2785&start_date=2023-01-01&end_date=2023-12-31&daily=daylight_duration,sunshine_duration&timezone=Asia%2FBangkok"

    response = requests.get(url).json()
    df = pd.DataFrame(response["daily"])
    checkData(df)

    avgSunshine = []
    avgDaylight = []

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
        monthData = df[monthLogic][["daylight_duration","sunshine_duration"]]

        stats = monthData.describe().round(3)
        daylight = ((stats.loc["mean", "daylight_duration"])//60)//60
        sunshine = ((stats.loc["mean", "sunshine_duration"])//60)//60
        
        avgSunshine.append(sunshine)
        avgDaylight.append(daylight)

    return avgSunshine, avgDaylight


if __name__ == "__main__":
    daylightAndSunshineDurationsChennai()
    daylightAndSunshineDurationsDelhi()
        





