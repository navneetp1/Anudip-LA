# 1. WAP to swap two integer values using third variable.
# def swap(x,y):
#     temp = x
#     x = y
#     y = temp
#     print(f"After swap x={x}, y={y}")

# x = int(input("Number 1: "))
# y = int(input("Number 2: "))
# print(f"Before swap x={x}, y={y}")
# swap(x,y)




# 2. WAP to swap two integer values without using third variable.

# def swap(x,y):
#     x = x+y
#     y = x-y
#     x = x-y
#     print(f"After swap x={x}, y={y}")

# x = int(input("Number 1: "))
# y = int(input("Number 2: "))
# print(f"Before swap x={x}, y={y}")
# swap(x,y)


# 3. WAP to convert temperature degree centigrade to degree Fahrenheit.

# temp = float(input("Enter temperature in celsius °C "))
# fahrenheit = float(((9/5)*temp) + 32)
# print(f"{temp}°C in Fahrenheit is {round(fahrenheit, 2)}")


# 6. WAP to calculate the total salary of an employee, where the basic salary of employee is 10,000
# and TA is 10%,DA is 20% and HRA is 30% of basic salary

basic = 10000
ta = 0.1*10000
da = 0.2*10000
hra = 0.3*10000
print(f"TA: Rs.{ta} DA: Rs. {da} HRA: {hra}")
