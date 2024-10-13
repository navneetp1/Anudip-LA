import requests
import numpy as np

# DELHI ONLY...

BASE_URL="https://archive-api.open-meteo.com/v1/archive?latitude=28.6519&longitude=77.2315&start_date=2023-01-01&end_date=2023-12-31&daily=temperature_2m_mean&timezone=Asia%2FBangkok"


url = BASE_URL

if __name__ == "__main__":

    response = requests.get(url).json()
    data = response

    dates = np.array(data['daily']['time'])
    daily_temp = np.array(data['daily']['temperature_2m_mean'])

    # print(dates)
    # print(daily_temp)

    # daywise temperatures for every month
    # january
    january = np.logical_and(dates >= "2023-01-01",dates <= "2023-01-31")
    january_day_wise = daily_temp[np.where(january)]

    print("Jan\n", january_day_wise)


    # february
    february = np.logical_and(dates >= "2023-02-01",dates <= "2023-02-28")
    february_day_wise = daily_temp[np.where(february)]

    print("\nFeb\n", february_day_wise)


    # march
    march = np.logical_and(dates >= "2023-03-01",dates <= "2023-03-31")
    march_day_wise = daily_temp[np.where(march)]

    print("\nMarch\n",march_day_wise)


    # april
    april = np.logical_and(dates >= "2023-04-01",dates <= "2023-04-30")
    april_day_wise = daily_temp[np.where(april)]

    print("\nApril\n",april_day_wise)

    #may
    may = np.logical_and(dates >= "2023-05-01",dates <= "2023-05-31")
    may_day_wise = daily_temp[np.where(may)]

    print("\nMay\n",may_day_wise)

    #june
    june = np.logical_and(dates >= "2023-06-01",dates <= "2023-06-30")
    june_day_wise = daily_temp[np.where(june)]

    print("\nJune\n",june_day_wise)

    #july
    july = np.logical_and(dates >= "2023-07-01",dates <= "2023-07-31")
    july_day_wise = daily_temp[np.where(july)]

    print("\nJuly\n",july_day_wise)


    #august
    august = np.logical_and(dates >= "2023-08-01",dates <= "2023-08-31")
    august_day_wise = daily_temp[np.where(august)]

    print("\nAugust\n",august_day_wise)


    #september
    september = np.logical_and(dates >= "2023-09-01",dates <= "2023-09-30")
    september_day_wise = daily_temp[np.where(september)]

    print("\nSeptemberil\n",september_day_wise)

    #october
    october = np.logical_and(dates >= "2023-10-01",dates <= "2023-10-31")
    october_day_wise = daily_temp[np.where(october)]

    print("\nOctober\n",october_day_wise)

    #november
    november = np.logical_and(dates >= "2023-11-01",dates <= "2023-11-30")
    november_day_wise = daily_temp[np.where(november)]

    print("\nNovember\n",november_day_wise)

    #december
    december = np.logical_and(dates >= "2023-12-01",dates <= "2023-12-31")
    december_day_wise = daily_temp[np.where(december)]

    print("\nDecember\n",december_day_wise)


        





