import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from EDA import checkData

def cityAverageTemperatures():
    def createAverageChart(city,avg):

        colors = ["#BEDFF1","#A0D1EC","#7EC4EF","#5CB6F2","#46ACF1","#3E9AD7"]
        fig, axs = plt.subplots(1, 1, figsize=(12, 10))

        barplot = axs.barh(city,avg, color=colors, linewidth=1.5, edgecolor="black")
        axs.set_xlabel("Average Temperatures(°C)")
        axs.set_ylabel("Cities")
        axs.set_title(f"Yearly averages of different cities in India")
        axs.bar_label(barplot, labels=avg, label_type="center")


        plt.show()
        plt.tight_layout()

    # BASE_URL = "https://archive-api.open-meteo.com/v1/archive?latitude=28.6519&longitude=77.2315&start_date=2023-01-01&end_date=2023-12-31&daily=temperature_2m_  mean&timezone=Asia%2FBangkok"

    BASE_URL = "https://archive-api.open-meteo.com/v1/archive?"

    # delhi, mumbai, chennai, kolkata, ahmedabad, shillong
    cities = ["Delhi","Mumbai", "Chennai", "Kolkata", "Ahmedabad", "Shillong"]

    lat = [28.6519,19.0728,13.0878,22.5626,23.0258,25.5689]

    lon = [77.2315,72.8826,80.2785,88.363,72.5873,91.8831]

    startDate = "2023-01-01"
    endDate = "2023-12-31"

    avgs = []

    for i in range(len(lat)):
        url = f"{BASE_URL}latitude={lat[i]}&longitude={lon[i]}&start_date={startDate}&end_date={endDate}&daily=temperature_2m_mean&timezone=Asia%2FBangkok"

        data = requests.get(url).json()
        daily_temp = np.array(data['daily']['temperature_2m_mean'])
        yearly_avg = np.mean(daily_temp).round(3)
        avgs.append(yearly_avg)

    avg_arr = np.array(avgs)
    city = np.array(cities)

    sorted = np.argsort(avg_arr)

    avg_arr = avg_arr[sorted]
    city = city[sorted]

    # print(city, avg_arr)
    # createAverageChart(city, avg_arr)


if __name__ == "__main__":
        BASE_URL = "https://archive-api.open-meteo.com/v1/archive?"
        lat = [28.6519,19.0728,13.0878,22.5626,23.0258,25.5689]

        lon = [77.2315,72.8826,80.2785,88.363,72.5873,91.8831]

        
        startDate = "2023-01-01"
        endDate = "2023-12-31"
        
        for i in range(len(lat)):
            url = f"{BASE_URL}latitude={lat[i]}&longitude={lon[i]}&start_date={startDate}&end_date={endDate}&daily=temperature_2m_mean&timezone=Asia%2FBangkok"
            data = requests.get(url).json()
            data = pd.DataFrame(data)
            checkData(data)










