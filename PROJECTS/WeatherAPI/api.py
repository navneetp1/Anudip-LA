import requests
import numpy as np

# DELHI ONLY...

BASE_URL="https://archive-api.open-meteo.com/v1/archive?latitude=28.6519&longitude=77.2315&start_date=2023-01-01&end_date=2023-12-31&daily=temperature_2m_mean&timezone=Asia%2FBangkok"


url = BASE_URL

def getWeatherData():
    response = requests.get(url).json()
    return response

def extractWeatherData(data):
    dates = np.array(data['daily']['time'])
    daily_temp = np.array(data['daily']['temperature_2m_mean'])

    def extractMonthData(startDate, endDate):
        month = np.logical_and(dates >= startDate,dates <= endDate)
        return daily_temp[np.where(month)]

    return {
        "january": extractMonthData("2023-01-01", "2023-01-31"),
        "february": extractMonthData("2023-02-01", "2023-02-28"),
        "march": extractMonthData("2023-03-01", "2023-03-31"),
        "april": extractMonthData("2023-04-01", "2023-04-30"),
        "may": extractMonthData("2023-05-01", "2023-05-31"),
        "june": extractMonthData("2023-06-01", "2023-06-30"),
        "july": extractMonthData("2023-07-01", "2023-07-31"),
        "august": extractMonthData("2023-08-01", "2023-08-31"),
        "september": extractMonthData("2023-09-01", "2023-09-30"),
        "october": extractMonthData("2023-10-01", "2023-10-31"),
        "november": extractMonthData("2023-11-01", "2023-11-30"),
        "december": extractMonthData("2023-12-01", "2023-12-31"),
    }

def averagePerMonth():
    data = getWeatherData()
    monthlyData = extractWeatherData(data)

    return {
        "january": np.mean(monthlyData["january"]).round(3),
        "february": np.mean(monthlyData["february"]).round(3),
        "march": np.mean(monthlyData["march"]).round(3),
        "april": np.mean(monthlyData["april"]).round(3),
        "may": np.mean(monthlyData["may"]).round(3),
        "june": np.mean(monthlyData["june"]).round(3),
        "july": np.mean(monthlyData["july"]).round(3),
        "august": np.mean(monthlyData["august"]).round(3),
        "september": np.mean(monthlyData["september"]).round(3),
        "october": np.mean(monthlyData["october"]).round(3),
        "november": np.mean(monthlyData["november"]).round(3),
        "december": np.mean(monthlyData["december"]).round(3),
    }


if __name__ == "__main__":
    data = getWeatherData()
    monthlyData = extractWeatherData(data)

    print("January\n", monthlyData["january"])
    print("\nFebruary\n", monthlyData["february"])
    print("\nMarch\n", monthlyData["march"])
    print("\nApril\n", monthlyData["april"])
    print("\nMay\n", monthlyData["may"])
    print("\nJune\n", monthlyData["june"])
    print("\nJuly\n", monthlyData["july"])
    print("\nAugust\n", monthlyData["august"])
    print("\nSeptember\n", monthlyData["september"])
    print("\nOctober\n", monthlyData["october"])
    print("\nNovember\n", monthlyData["november"])
    print("\nDecember\n", monthlyData["december"])

    print(averagePerMonth())
