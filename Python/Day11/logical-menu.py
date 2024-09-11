print("Logical Programs | Select your program")
choice = "y"

def evenGen():
    num = int(input("Enter value of n: "))
    print("Even Number Generator")
    for i in range(0, num+1):
        if i%2 == 0:
            print(i, " ")
   
def oddGen():
    num = int(input("Enter value of n: "))
    print("Odd Number Generator")
    for i in range(1, num+1):
        if i%2 != 0:
            print(i, " ")

def primeNumberGen():
    flag=0
    num = int(input("Enter the upper bound: "))
    print(f"All the prime numbers until {num} are displayed below")
    for i in range(2, num):
        for j in range(2,i):
            if (i % j == 0):
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            print(i, end=" ")

def factGen():
    num = int(input("Enter number whose factorial is to be calculated: "))
    print("Factorial Generator")
    fact = 1
    real = num
    while(num > 0):
        fact = fact * num
        num -= 1
    print(f"Factorial of {real}: ", fact)

def fibSeries():
    def fib(x):
        if x == 1:
            return 1
        if x == 0:
            return 0
        else:
            return fib(x-1)+fib(x-2)
    
    fibInput = int(input("Enter n until where you want the series: "))
    print(f"Fibonacci Series upto {fibInput}")

    for i in range(fibInput):
        print(fib(i), end=" ")

def floydTriangle():
    num = int(input("Enter no of rows: "))
    print(f"Floyd's Triangle with rows = {num}")
    n = 1
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(n, end=" ")
            n+=1    
        print("")
        
def pascalTriangle():
    def factorial(n):
        fact = 1
        while n > 0:
            fact = fact * n
            n-=1
        return fact
    num = int(input("Enter no of rows: "))
    print(f"Pascal's Triangle for rows = {num}")
    for i in range(num):
        for j in range(num-i+1):
            print(end=" ") 
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()

def armstrongNum():
    num = int(input("Enter a number having atleast 3 digits(eg: 153, 370): "))
    print("Armstrong numbers are those whose individual digit cubes sum is equal to the number")
    sum = 0
    t = num
    while t > 0:
        digit = t % 10
        sum += (digit * digit * digit)
        t = t // 10

    if num == sum:
        print(f"{num} is an Armstrong Number")
    else:
        print("It's not an Armstrong number")

def palindromeChecker():
    str = input("Enter a string: ")
    reverse = str[::-1]
    if str == reverse:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
    

while choice == "y":
    print("++++++++++++++++++++++++++++++")
    print("1. Even Number Generation")
    print("2. Odd Number Generation")
    print("3. Prime Number Generation")
    print("4. Factorial Generation")
    print("5. Fibonacci Series")
    print("6. Flody Triangle")
    print("7. Pascal Triangle")
    print("8. Armstrong Number")
    print("9. String Palindrome Checker")
    print("++++++++++++++++++++++++++++++")

    option = int(input("Enter your choice(1-9): "))

    match option:
        case 1: 
            evenGen()
        case 2: 
            oddGen()
        case 3: 
            primeNumberGen()
        case 4: 
            factGen()
        case 5: 
            fibSeries()
        case 6: 
            floydTriangle()
        case 7: 
            pascalTriangle()
        case 8: 
            armstrongNum()
        case 9: 
            palindromeChecker()
        case _: 
            print("Invalid choice!!")
    choice = input("\nWant to continue?(y/n): ")

    if not choice == "y":
        break