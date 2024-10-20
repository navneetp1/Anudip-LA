# temperature vs humidity scatterplot in delhi vs chennai
import requests
import pandas as pd




def scatterplotDelhi():
    
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=28.6519&longitude=77.2315&start_date=2023-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m&timezone=Asia%2FBangkok"


    response = requests.get(url).json()
    df = pd.DataFrame(response["hourly"])

    tempWithHumidity = {}

    startTime = [
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

    endTime = [
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

    for i in range(len(endTime)):
        monthLogic = (df["time"] >= startTime[i]) & (df["time"] <= endTime[i])
        monthData = df[monthLogic][["temperature_2m","relative_humidity_2m"]]

        stats = monthData.describe().round(3)
        temp = stats.loc["mean", "temperature_2m"]
        humid = stats.loc["mean", "relative_humidity_2m"]
        tempWithHumidity[temp] = humid

        # print(stats.loc["mean", "temperature_2m"])
        # print(stats.loc["mean", "relative_humidity_2m"])

    return tempWithHumidity

# temperature vs humidity scatterplot in delhi vs chennai
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def scatterplotChennai():
    
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=13.0878&longitude=80.2785&start_date=2023-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m&timezone=Asia%2FBangkok"

    response = requests.get(url).json()
    df = pd.DataFrame(response["hourly"])

    tempWithHumidity = {}

    startTime = [
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

    endTime = [
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

    for i in range(len(endTime)):
        monthLogic = (df["time"] >= startTime[i]) & (df["time"] <= endTime[i])
        monthData = df[monthLogic][["temperature_2m","relative_humidity_2m"]]

        stats = monthData.describe().round(3)
        temp = stats.loc["mean", "temperature_2m"]
        humid = stats.loc["mean", "relative_humidity_2m"]
        tempWithHumidity[temp] = humid

        # print(stats.loc["mean", "temperature_2m"])
        # print(stats.loc["mean", "relative_humidity_2m"])

    return tempWithHumidity









