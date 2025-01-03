from api import extractWeatherData, getWeatherData, averagePerMonth
from scatterApi import scatterplotDelhi, scatterplotChennai
from cityAvg import cityAverageTemperatures
from daySunshine import daylightAndSunshineDurationsChennai, daylightAndSunshineDurationsDelhi
from sunriseSunset import sunriseAndSunsetDelhi, sunriseAndSunsetChennai
from minmax import maxMinTempChennai, maxMinTempDelhi
from extractData import fetchData
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta



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
    for a, b in zip(days, y):
        axs[0].text(a-0.5, b+0.2, f" {b} ", fontsize=8, ha="center", va="bottom")

    barplot = axs[1].bar(days,y)
    axs[1].set_xlabel("Day of the Month")
    axs[1].set_ylabel("Temperature(°C)")
    axs[1].set_title(f"Daily Temperature in {month}")
    axs[1].bar_label(barplot, labels=y, rotation=90, fontsize=9)


    plt.tight_layout()
    plt.show()

def chooseMonth():
    month = input("Enter month: ").lower()
    monthData = monthlyData[month]

    createChart(month, monthData.size, monthData)




def createAverageChart(monthAvg):
    months = np.array(list(monthAvg.keys()))
    avgs = np.array(list(monthAvg.values()))

    fig, axs = plt.subplots(1,2, figsize=(12, 10))
    axs[0].plot(months, avgs, marker="D")
    axs[0].grid()

    axs[0].set_xlabel("Month of the Year")
    axs[0].set_ylabel("Average Temperatures(°C)")
    axs[0].set_title(f"Average Temperatures over the year")
    axs[0].tick_params(axis="x",rotation=45)
    for a, b in zip(months, avgs):
        axs[0].text(a, b+0.2, f" {b} ", fontsize=8, ha="center", va="bottom")

    barplot = axs[1].barh(months,avgs, color="skyblue", linewidth=1.5, edgecolor="black")
    axs[1].set_xlabel("Average Temperatures")
    axs[1].set_ylabel("Months")
    axs[1].set_title(f"Average Temperatures over the year")
    axs[1].bar_label(barplot, labels=avgs, label_type="center")


    
    plt.tight_layout()
    plt.show()




def createScatterPlot(x,y, city):
    xValues = x
    yValues = y
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # print(xValues, yValues)

    for i,(a,b) in enumerate(zip(xValues, yValues)):
        plt.text(a,b+1,f"{months[i]}|{a}|{b}", fontsize=8, ha="center")
    
    plt.scatter(xValues, yValues, marker="o")
    plt.xlabel("Temperatures(°C)")
    plt.ylabel("Relative Humidity(%)")
    plt.title(f"Scatter Plot of Temperature vs Humidity [{city} 2023]")

    plt.grid()
    plt.tight_layout()
    plt.show()



def createBarhChart(values, quantityName, place):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    x = values

    barplot = plt.barh(months, x, color="skyblue", linewidth=1.5, edgecolor="yellow")
    plt.xlabel(f"{quantityName} in hours")
    plt.ylabel("Months")
    plt.bar_label(barplot, labels=x, label_type="center")
    plt.title(f"Average {quantityName} hours for {place} in 2023")

    plt.tight_layout()
    plt.show()




def sunriseSunsetPlot(sunrise,sunset,place):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sunriseTimes = sunrise
    sunsetTimes = sunset
   

    sunrise = [datetime.combine(datetime(1970, 1, 1), t) for t in sunriseTimes]
    sunset = [datetime.combine(datetime(1970, 1, 1), t) for t in sunsetTimes]

    plt.figure(figsize=(10, 6))

    plt.plot(months, sunrise, label="Sunrise", color='orange', marker='o')
    for i,x in enumerate(sunrise):
        plt.text(i,x+timedelta(minutes=5),f"{x.strftime('%H:%M')}", fontsize=8, ha="center")
    
    plt.plot(months, sunset, label="Sunset", color='blue', marker='o')
    for i,x in enumerate(sunset):
        plt.text(i,x+timedelta(minutes=5),f"{x.strftime('%H:%M')}", fontsize=8, ha="center")

    # Fill between sunrise and sunset to show daylight hours
    plt.fill_between(months, sunrise, sunset, color='skyblue', alpha=0.3)

    # Formatting the y-axis to show time in HH:MM format
    plt.gca().yaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M'))

    # Rotate x-axis labels for better readability
    plt.gcf().autofmt_xdate()

    
    plt.xlabel("Month")
    plt.ylabel("Time of Day (24-hour format)")
    plt.title(f"Average Sunrise and Sunset Times for Each Month[{place} 2023]")
    plt.legend()

    plt.tight_layout()
    plt.show()




def dualBarPlot(maximum, minimum, place):
    maxTemps = maximum
    minTemps = minimum
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    width = 0.25  # the width of the bars
    x = np.arange(len(months))
    multiplier = 0
    colors = ["#88CCEE", "#DDCC77"]

    fig, ax = plt.subplots(layout='constrained')

    for measurement,label,color in zip([maxTemps, minTemps], ["Max Temperatures", "Min Temperatures"], colors):
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=label, color=color, edgecolor="black", linewidth=1.1)
        ax.bar_label(rects, padding=3)
        multiplier += 1

  
    ax.set_ylabel('Temperature(°C)')
    ax.set_title(f"Monthly Maximum and Minimum Temperatures [{place} 2023]")
    ax.set_xticks(x + width / 2, months)
    ax.legend(loc='upper left')
    ax.set_ylim(0, 60)

    plt.show()



def saveToCSV():
    temperatures, humidity, sunrises, sunsets, sunshineDurations, daylightDurations, maxTemperatures, minTemperatures = fetchData()
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    try:
        filtered = pd.DataFrame({
            "Months": months,
            "Temperatures": temperatures,
            "Humidity": humidity,
            "Sunrise Times": sunrises,
            "Sunset Times": sunsets,
            "Sunshine Durations": sunshineDurations,
            "Daylight Durations": daylightDurations,
            "Maximum Temp": maxTemperatures,
            "Minimum Temp": minTemperatures,
        })

        filename = input("Enter the name of the file(don't add extension): ")

        filtered.to_excel(f"{filename}.xlsx", index=False)
    except:
          print("Some error occurred while creating file")
    finally:
          print("File has been created successfully.")

    

def choiceMenu():
    while True:
        print("--|--Weather Statistics Menu--|--")
        print("--|--All the graphs are based upon 2023 Weather Information--|--\n")
        print("1.  Day-wise Temperatures of any Month in Delhi")
        print("2.  Average Monthly Temperatures in Delhi")
        print("3.  Average Yearly Temperatures for different cities in India")
        print("4.  Scatterplot between Temperature and Humidity for Delhi(2023)")
        print("5.  Scatterplot between Temperature and Humidity for Chennai(2023)")
        print("6.  Sunshine and Daylight Durations in Delhi(2023)")
        print("7.  Sunshine and Daylight Durations in Chennai(2023)")
        print("8.  Sunrise and Sunset Times in Delhi(2023)")
        print("9.  Sunrise and Sunset Times in Chennai(2023)")
        print("10. Maximum and Minimum Temperatures per month in Delhi(2023)")
        print("11. Maximum and Minimum Temperatures per month in Chennai(2023) ")
        print("12. Save data to Excel file")
        
        print("13. Exit")
        choice = input("Enter your choice (1-13): ")

        match choice:
            case '1':
                    print("You chose the first option!")
                    chooseMonth()
            case '2':
                    print("You chose the second option!")
                    createAverageChart(monthlyAverages)
            case '3':
                    print("You chose the third option!")
                    # path=os.path.abspath("city-avg.py")
                    cityAverageTemperatures()
            case '4':
                    print("You chose the fourth option!")
                    x = np.array(list(scatterplotDelhi().keys()))
                    y = np.array(list(scatterplotDelhi().values()))
                    createScatterPlot(x,y, "DELHI")
            case '5':
                    print("You chose the fith option!")
                    x = np.array(list(scatterplotChennai().keys()))
                    y = np.array(list(scatterplotChennai().values()))
                    createScatterPlot(x,y, "CHENNAI")
            case '6': 
                    sunshine,daylight = daylightAndSunshineDurationsDelhi()
                    createBarhChart(sunshine, "Sunshine", "DELHI")
                    createBarhChart(daylight, "Daylight", "DELHI")
            case '7': 
                    sunshine2, daylight2 = daylightAndSunshineDurationsChennai()
                    createBarhChart(sunshine2, "Sunshine", "CHENNAI")
                    createBarhChart(daylight2, "Daylight", "CHENNAI")
            case '8':
                    sunrise, sunset = sunriseAndSunsetDelhi()
                    sunriseSunsetPlot(sunrise, sunset, "DELHI")
            case '9':
                    sunriseChen, sunsetChen = sunriseAndSunsetChennai()
                    sunriseSunsetPlot(sunriseChen, sunsetChen, "CHENNAI")
            case '10': 
                    minTemps, maxTemps = maxMinTempDelhi()
                    dualBarPlot(maxTemps, minTemps, "DELHI")
            case '11': 
                    minTempsChen,maxTempsChen = maxMinTempChennai()
                    dualBarPlot(maxTempsChen, minTempsChen, "CHENNAI")
            case '12':
                    saveToCSV()
            case '13':
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
