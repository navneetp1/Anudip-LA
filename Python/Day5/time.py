# Write a program that uses an IF statement to print "Good morning" if the time is between 5 and 12 hours in a 24-hour format.
# Example: 2:00 PM will be 14 in 24-hour format.

import time
# parts=[]
# print(time.time())

# t = time.localtime()
# format_time = time.strftime("%H:%M:%S", t)
# parts = format_time.split(":")
# print(parts)

# print(format_time)
import time
t = time.localtime()
hours = int(time.strftime("%H",t))
mins = int(time.strftime("%M",t))

if(hours > 5 and hours<12 and mins <= 59):
    print("Good morning")


age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
elif age == 18:
    print("Congratulations on your first vote!")
else:
    print("Sorry, you are not eligible to vote.")