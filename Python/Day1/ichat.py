# Write a Python script to greet guests at an event based on the time of their arrival and their personal greeting preference.
# Your script should include a function that takes three parameters:
# the guest's name
# their arrival time in a 24-hour format
# whether they prefer a 'formal' or 'informal' greeting.
# Depending on the time of day (morning before noon, afternoon before 18:00, evening after 18:00) and the guest's preference, the function should print a customized greeting message. Include a list of guests with their names, arrival times, and preferences, and ensure your script can greet each guest appropriately when run.
# Provide a function to loop through a list of guests and apply the greeting function to each.

# Ensure your script correctly handles the time-based greeting logic and guest preferences and prints the appropriate message for each guest based on the provided data.


# Use the following guest data for testing:
# > James arrives at 11 and prefers a formal greeting.

# > Jacob arrives at 11 and prefers a formal greeting.

# > Benjamin arrives at 14 and prefers an informal greeting.

# > William arrives at 19 and prefers a formal greeting.

# > Alexander arrives at 20 and prefers an informal greeting.

# guests = ["James", "Jacob", "Benjamin", "William", "Alexander"]
# times = [11,11,14,19,20]
# greetTypes = ["formal","formal","informal","formal","informal"]



# def checkType(type, time):
#     if type == "formal":
#         if time < 12:
#             return "Good Morning"
#         elif 12 < time < 18:
#             return "Good Afternoon"
#         else:
#             return "Good Evening"
#     else:
#         if time < 12:
#             return "Hey, morning!"
#         elif 12 < time < 18:
#             return "Hey, afternoon!"
#         else:
#             return "Hey handsome, evening Top G"

# def greet(guests,times,greet):
#     for i in range(len(times)):
#         greetType = checkType(greet[i], times[i])
#         print(f"{greetType} {guests[i]}")

# greet(guests,times,greetTypes)

# guests = [
# {"name": "James", "arrival_time": 11, "preference": "formal"},
# {"name": "Jacob", "arrival_time": 11, "preference": "formal"},
# {"name": "Benjamin", "arrival_time": 14, "preference": "informal"},
# {"name": "William", "arrival_time": 19, "preference": "formal"},
# {"name": "Alexander", "arrival_time": 20, "preference": "informal"}
# ]

# def greet_guest(name, arrival_time, greeting_preference):
#     if arrival_time < 12:
#         time_of_day = "morning"
#     elif arrival_time < 18:
#         time_of_day = "afternoon"
#     else:
#         time_of_day = "evening"

#     if greeting_preference == "formal":
#         greeting = f"Good {time_of_day}, Mr./Ms. {name}."
#     else:
#         greeting = f"Hey {name}, good {time_of_day}!"
#     print(greeting)
    
# def greet_all_guests(guest_list):
#     for guest in guest_list:
#         greet_guest(guest["name"], guest["arrival_time"], guest["preference"])
# greet_all_guests(guests)


# def convert_to_fahrenheit(celsius):
#     try:
#         celsius = float(celsius)
        
#         fahrenheit = celsius * 9/5 + 32
#         return fahrenheit
    
#     except ValueError:
#         return "Invalid input, Please enter a numeral"

# # Example usage
# print(convert_to_fahrenheit(25))  # Valid input
# print(convert_to_fahrenheit("twenty-five"))  # Invalid input


def calculate_total_cost(base_cost, tax_rate, tip_percentage):
    try:
        # Convert inputs to float and validate they are positive numbers
        base_cost = float(base_cost)
        tax_rate = float(tax_rate)
        tip_percentage = float(tip_percentage)
        
        # Check for negative or extremely high values
        if base_cost < 0:
            return "Invalid input: Base cost cannot be negative."
        if not (0 <= tax_rate <= 100):
            return "Invalid input: Tax rate must be between 0 and 100."
        if not (0 <= tip_percentage <= 100):
            return "Invalid input: Tip percentage must be between 0 and 100."
        
        # Calculate the tax and tip
        tax_amount = base_cost * (tax_rate / 100)
        tip_amount = base_cost * (tip_percentage / 100)
        
        # Calculate the total cost
        total_cost = base_cost + tax_amount + tip_amount
        
        return round(total_cost, 2)
    
    except ValueError:
        return "Invalid input: Please provide numeric values for all inputs."

# Example usage
print(calculate_total_cost(100, 10, 15))  # Valid input: 100 base, 10% tax, 15% tip
print(calculate_total_cost("100", "10", "15"))  # Valid string input
print(calculate_total_cost(-100, 10, 15))  # Invalid base cost (negative)
print(calculate_total_cost(100, 150, 15))  # Invalid tax rate (over 100%)
print(calculate_total_cost(100, 10, -15))  # Invalid tip percentage (negative)
print(calculate_total_cost("abc", 10, 15))  # Invalid non-numeric input

