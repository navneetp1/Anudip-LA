import requests
import pandas as pd

def maxMinTemp():
    url="https://archive-api.open-meteo.com/v1/archive?latitude=28.6519&longitude=77.2315&start_date=2023-01-01&end_date=2023-12-31&daily=temperature_2m_max,temperature_2m_min&timezone=Asia%2FBangkok"
    response = requests.get(url).json()
    df = pd.DataFrame(response["daily"])

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

    # print(df.columns)
    logic = (df["time"] >= "2023-01-01") & (df["time"] <= "2023-12-31")
    temps = df[logic]


maxMinTemp()