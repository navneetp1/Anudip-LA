from main import extractWeatherData, getWeatherData, averagePerMonth
import matplotlib.pyplot as plt
import numpy as np

delhiData = getWeatherData()
monthlyAveragesForDelhi = averagePerMonth()

mumbaiData = getWeatherData()
monthlyAveragesForMumbai = averagePerMonth()

chennaiData = getWeatherData()
monthlyAveragesForChennai = averagePerMonth()

kolkataData = getWeatherData()
monthlyAveragesForKolkata = averagePerMonth()

AhmedabadData = getWeatherData()
monthlyAveragesForAhmedabad = averagePerMonth()







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


# createAverageChart(monthlyAveragesForAhmedabad)

print(monthlyAveragesForDelhi) 
print(monthlyAveragesForMumbai) 
print(monthlyAveragesForChennai) 
print(monthlyAveragesForKolkata) 
print(monthlyAveragesForAhmedabad) 
    





