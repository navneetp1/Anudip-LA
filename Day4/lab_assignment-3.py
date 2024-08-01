
# Q1. Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

def checkNum(num):
    if(num==0):
        print(f"0 is neither even nor odd")
    else:
        rem = num % 2
        match rem:
            case 0:
                print(f"Even")
            case 1:
                print(f"Odd")
            case _:
                print("Number invalid")

number = int(input("Enter a number: "))
checkNum(number)


# output:
#       Enter a number: 0
#       0 is neither even nor odd
#       Enter a number: 34
#       Even


# ---------------------------------------------------------------------------------------------

#Q 2. Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

def checkEligibility(age):
    match age:
        case _ if age < 0:
            print("Invalid age")
        case _ if age >=18:
            print("You are eligible to vote!!")
        case _ if age<18:
            print("Sorry, you are not eligible to vote")

age = int(input("Please enter your age: "))
checkEligibility(age)

# output: 
#       Please enter your age: 18
#       You are eligible to vote!!
#       Please enter your age: -2
#       Invalud age
#       Please enter your age: 12
#       Sorry, you are not eligible to vote


# ---------------------------------------------------------------------------------------------




# Q 3.  Write a Python program that determines if a given year is a leap year or not.

def checkLeap(year):
   if(year%4 == 0 and year%100 != 0 or year%400 == 0):
       return True
   return False

year = int(input("Enter an year: "))
if(checkLeap(year)):
    print("It's a leap year")
else:
    print("It's not a leap year")

# output: 
#       Enter an year: 1990
#       It's not a leap year
#       Enter an year: 2020
#       It's a leap year
#       Enter an year: 2050
#       It's not a leap year




# ---------------------------------------------------------------------------------------------



# Q 4.  Create a Python program that checks if a user-given number is positive, negative, or zero.

def checkNum(num):
    match num:
        case _ if num == 0:
            print("The number is 0")
        case _ if num < 0:
            print("It's a negative number")
        case _ if num > 0:
            print("It's a positive number")
        case _: print("Invalid number")

number = int(input("Enter an integer: "))
checkNum(number)

# output: Enter an integer: 12
        # It's a positive number
        # Enter an integer: -34
        # It's a negative number
        # Enter an integer: 0
        # The Number is 0


# ---------------------------------------------------------------------------------------------



# Q 5.  Write a Python program that determines the largest of three numbers entered by the user.

a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))

if(a>b):
    if(a>c):
        print(f"{a} is the largest")
    else:
        print(f"{c} is the largest")
else:
    if(b>c):
        print(f"{b} is the largest")
    else:
        print(f"{b} is the largest")

# output: 
#       Enter number 1: 5
#       Enter number 2: 6
#       Enter number 3: 2
#       6 is the largest


# ---------------------------------------------------------------------------------------------

# pattern homework
# A -> 1
# #    12
# #    123
# #    1234
# #    12345

# B -> 5
#      45
#      345
#      2345
#      12345


n = int(input("Enter a number: ")) # accounting for dynamimc values
# put n = 5 for the required result

# A 
for i in range(1,n+1):
    for j in range(1,i):
        print(j, end=' ')
    print(i)

# B 
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j, end=' ')
    print()


# C ->  1 2
#       1 2 3
# put n = 2 for required result
for i in range(1,n+1):
    for j in range(1, i+2):
        print(j, end=" ")
    print()


