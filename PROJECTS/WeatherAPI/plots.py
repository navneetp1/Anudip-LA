from api import extractWeatherData, getWeatherData, averagePerMonth
import matplotlib.pyplot as plt
import numpy as np
from subprocess import call

data = getWeatherData()

monthlyData = extractWeatherData(data)
monthlyAverages = averagePerMonth()

def createChart(month,x,y):
    days = np.arange(1,x+1)

    fig, axs = plt.subplots(1, 2, figsize=(12, 10))
    axs[0].plot(days, y,marker="D")
    axs[0].grid()

    axs[0].set_xlabel("Day of the Month")
    axs[0].set_ylabel("Temperature(°C)")
    axs[0].set_title(f"Daily Temperature in {month}")

    barplot = axs[1].bar(days,y)
    axs[1].set_xlabel("Day of the Month")
    axs[1].set_ylabel("Temperature(°C)")
    axs[1].set_title(f"Daily Temperature in {month}")
    axs[1].bar_label(barplot, labels=y, rotation=90, fontsize=9)


    plt.show()
    plt.tight_layout()

def chooseMonth():
    month = input("Enter month: ")
    monthData = monthlyData[month]

    createChart(month, monthData.size, monthData)

######################################################


def createAverageChart(monthAvg):
    months = np.array(list(monthAvg.keys()))
    avgs = np.array(list(monthAvg.values()))

    fig, axs = plt.subplots(1, 2, figsize=(12, 10))
    axs[0].plot(months, avgs, marker="D")
    axs[0].grid()

    axs[0].set_xlabel("Month of the Year")
    axs[0].set_ylabel("Average Temperatures(°C)")
    axs[0].set_title(f"Average Temperatures over the year")
    axs[0].tick_params(axis="x",rotation=45)

    barplot = axs[1].barh(months,avgs, color="skyblue", linewidth=1.5, edgecolor="black")
    axs[1].set_xlabel("Average Temperatures")
    axs[1].set_ylabel("Months")
    axs[1].set_title(f"Average Temperatures over the year")
    axs[1].bar_label(barplot, labels=avgs, label_type="center")


    plt.show()
    plt.tight_layout()


#################################
def choiceMenu():
    while True:
        print("--|--Weather Statistics Menu--|--")
        print("1. Day-wise Temperatures of any Month")
        print("2. Average Monthly Temperatures")
        print("3. Average Yearly Temperatures for different cities in India")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        match choice:
            case '1':
                print("You chose the first option!")
                chooseMonth()
            case '2':
                print("You chose the second option!")
                createAverageChart(monthlyAverages)
            case '3':
                print("You chose the third option!")
                call(["python",r"C:\Python Programs\WeatherAPI\city-avg.py"])
            case '4':
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")
                continue

        # Ask if the user wants to continue
        continue_choice = input("\nDo you want to continue? (y/n): ").lower()
        if continue_choice != 'y':
            print("Exiting the menu.")
            break

choiceMenu()

    


    





