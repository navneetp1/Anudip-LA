from datetime import time

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
attributes = ["Temperatures", "Humidity", "Sunrise_Times", "Sunset_Times", "Sunshine_Hours", "Daylight_Hours", "Max_Temp", "Min_Temp"]
temperatures = [11.745, 17.983, 21.723, 27.095, 29.149, 31.048, 28.931, 30.27, 28.946, 25.039, 19.832, 14.99]
humidity = [80.925, 62.958, 61.319, 38.062, 46.722, 59.451, 82.386, 69.472, 72.671, 58.817, 71.572, 75.259]
Sunrises = [time(8, 42), time(8, 28), time(7, 59), time(7, 25), time(7, 0), time(6, 52), time(7, 3), time(7, 19), time(7, 35), time(7, 51), time(8, 13), time(8, 35)]
Sunsets = [time(19, 15), time(19, 39), time(19, 58), time(20, 16), time(20, 34), time(20, 49), time(20, 49), time(20, 28), time(19, 55), time(19, 20), time(18, 57), time(18, 56)]
sunshineDurations = [8.0, 10.0, 9.0, 10.0, 9.0, 9.0, 8.0, 10.0, 10.0, 10.0, 8.0, 8.0]
daylightDurations = [10.0, 11.0, 11.0, 12.0, 13.0, 13.0, 13.0, 13.0, 12.0, 11.0, 10.0, 10.0]
maxTemp = [22.7, 30.5, 32.3, 39.7, 43.2, 41.9, 36.2, 36.7, 38.2, 35.4, 30.5, 24.5]
minTemp = [2.9, 9.0, 13.7, 15.2, 18.6, 19.8, 23.6, 24.5, 20.0, 16.0, 10.4, 6.6]

# record = 1

# for j in range(len(months)):  # Single loop over the months
#     print(
#         f"Record ID: {record}, Month ID: {j+1}, Month: {months[j]}, "
#         f"Temperature: {temperatures[j]}, Humidity: {humidity[j]}, "
#         f"Sunrise Time: {Sunrises[j]}, Sunset Time: {Sunsets[j]}, "
#         f"Sunshine Duration: {sunshineDurations[j]}, Daylight Duration: {daylightDurations[j]}, "
#         f"Max Temp: {maxTemp[j]}, Min Temp: {minTemp[j]}"
#     )
#     record += 1

# for i,month in enumerate(months):
#     print(f"{i+1}, {month}")

record = 1
for i in range(len(months)):
    for j in range(len(attributes)):
        print(f"insert into table values ({record}, {i+1}, {j+1}, {temperatures[j]}, {humidity[j]}, {Sunrises[j]}, {Sunsets[j]}, {sunshineDurations[j]}, {daylightDurations[j]}, {maxTemp[j]}, {minTemp[j]})")
        record += 1