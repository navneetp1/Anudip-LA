# Q 1. Function without Parameters:

def samplePrintFunction():
    print("Hey this function takes no parameters.")

def operationsWithTwoDefinedValues():
    a,b = 2,4
    print(f"Sum of {a} and {b} is", a+b)
    print(f"Difference of {a} and {b} is", a-b)
    print(f"Product of {a} and {b} is", a*b)

samplePrintFunction()
operationsWithTwoDefinedValues()

# output
#       Hey this function takes no parameters.
#       Sum of 2 and 4 is 6
#       Difference of 2 and 4 is -2
#       Product of 2 and 4 is 8


# ----------------------------------------------------------------------------


# Q 2. Function with Parameter:

def calculateSum(x,y):
    print(f"Sum of {x} and {y} is {x+y}")

def cube(a):
    return a*a*a

def greetFunction(firstName, lastName, occupation):
    print(f"Good Evening, {firstName} {lastName}. Your occupation is {occupation}")

calculateSum(2,5)
greetFunction("Sharon", "Williams", "Contractor")
print(cube(45))

# output 
#       Sum of 2 and 5 is 7
#       Good Evening, Sharon Williams. Your occupation is Contractor
#       91125

# ----------------------------------------------------------------------------

# Q 3.  Function with Default Parameter:

def calculateSimpleInterest(principal = 10000, rate = 10, time=1):
    result = principal * float(rate/100) * time
    return result

print(f"Simple Interest with default values: Rs.{calculateSimpleInterest()}")

newPrincipal = int(input("Enter a principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))
print(f"SI with principal = {newPrincipal} rate = {rate}% time = {time} years: Rs.{calculateSimpleInterest(newPrincipal,rate,time)}")

# output
#       Simple Interest with default values: Rs.1000.0
#       Enter a principal amount: 23500
#       Enter rate of interest: 15
#       Enter time in years: 4
#       SI with principal = 23500 rate = 15% time = 4 years: Rs.14100.0

#  ----------------------------------------------------------------------------

# Q 4.  Function with Return Keyword:

def compoundInterestAmount(principal, rate,n, time):
    amount = principal*(1+(rate/(n*100)))**(n*time)
    return amount

principal = int(input("Enter principal amount: "))
rate = int(input("Enter rate of interest: "))
n = int(input("Enter the number of times interest is compounded per year: "))
time = int(input("Enter the time in years: "))

compoundInterest = compoundInterestAmount(principal, rate,n,time) - principal
print(f"Compounded Interest Amount is: Rs. {round(compoundInterest,3)}")

# output
#       Enter principal amount: 34500
#       Enter rate of interest: 12
#       Enter the number of times interest is compounded per year: 4
#       Enter the time in years: 5
#       27810.838


#  ----------------------------------------------------------------------------


# 5.  Recursion:

def factorial(x):
    if(x<=1):
        return 1
    return x * factorial(x-1)

def fibNums(y):
    if y == 0:
        return 0
    if y == 1:
        return 1
    
    return fibNums(y-1)+fibNums(y-2)


num = int(input("Enter number to calculate its factorial: "))
fibInput = int(input("Enter no of terms for fibonacci series: "))


print(f"Factorial of {num} is {factorial(num)}")

for i in range(fibInput):
    print(fibNums(i), end=" ")


# output: 
#       Enter number to calculate its factorial: 10
#       Enter no of terms for fibonacci series: 15
#       Factorial of 10 is 3628800
#       0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

