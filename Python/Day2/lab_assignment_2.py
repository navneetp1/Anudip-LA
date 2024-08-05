# Q.1 Write a program for arithmetic operators

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    print(f"Addition: {num1+num2}")
    print(f"Subtraction: {num1-num2}")
    print(f"Multiplication: {num1*num2}")
    print(f"Division: {num1/num2}")
    print(f"Remainder: {num1-num2}")
    print(f"Floor Division: {num1//num2}")
    print(f"Exponentiaion: {num1**num2}")
except ValueError:
    print("Input is not a valid number")

# output
#       Enter a number: 45
#       Enter a number: 9
#       Addition: 54
#       Subtraction: 36
#       Multiplication: 405
#       Division: 5.0
#       Remainder: 36
#       Floor Division: 5
#       Exponentiaion: 756680642578125

# ----------------------------------------------------------------------


# Q.2 Write a program for assignment operators

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    result = num1 + num2
    print(f"Result is assigned the sum of {num1} and {num2} which is {result}")
    result += 15
    result -= 1
    print(f"New result: {result}")
except ValueError:
    print("Input is not a valid number")

# ouput: Enter a number: 45
    #    Enter a number: 45
    #    Result is assigned the sum of 45 and 45 which is 90
    #    New result: 104


# ----------------------------------------------------------------------


# Q.3 Write a program for Bitwise operators 

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

bAND = a & b
bOR = a | b
neg = ~a
bXOR = a ^ b
right = a >> b
left = a << b

print(f"Binary of {a} = {bin(a)}\nBinary of {b} = {bin(b)}")
print(f"Bitwise AND is {bAND}, in binary = {bin(bAND)}")
print(f"Bitwise OR is {bOR}, in binary = {bin(bOR)}")
print(f"Bitwise NOT of {a} is {neg}, in binary = {bin(neg)}")
print(f"Bitwise XOR is {bXOR}, in binary = {bin(bXOR)}")
print(f"Bitwise Right shift is {right}, in binary = {bin(right)}")
print(f"Bitwise Left shift is {left}, in binary = {bin(left)}")

# output: Enter number 1: 12 
#         Enter number 2: 4
#         Binary of 12 = 0b1100
#         Binary of 4 = 0b100
#         Bitwise AND is 4, in binary = 0b100
#         Bitwise OR is 12, in binary = 0b1100
#         Bitwise NOT of 12 is -13, in binary = -0b1101
#         Bitwise XOR is 8, in binary = 0b1000
#         Bitwise Right shift is 0, in binary = 0b0
#         Bitwise Left shift is 192, in binary = 0b11000000

# ----------------------------------------------------------------------


# Q.4 Write a program to calculate greatest of three numbers.

try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = int(input("Enter number 3: "))

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
except ValueError:
    print("Input is not a valid number") 

# output: Enter number 1: 4
#         Enter number 2: 5
#         Enter number 3: 2
#         5 is the largest

# ----------------------------------------------------------------------



# 1.      Calculate the area of a circle.

def calcArea(rad):
    return 3.14 * (rad ** 2)

try:
    radius = float(input("Input a valid radius: "))
    area = calcArea(radius)
    print(f"Area of circle with given radius {radius} is {round(area, 3)} square units")
except ValueError:
    print("Input is not a valid number")

# output: Input a valid radius: 45.32 
#         Area of circle with given radius 45.32 is 6449.254 square units

# ----------------------------------------------------------------------


# 2.      Calculate the area of a triangle.

def calcArea(b, h):
    return .5 * (b * h)

try:
   base = float(input("Enter a valid base value: "))
   height = float(input("Enter a valid height value: "))

   area = calcArea(base, height)
   print(f"Area of the given triangle is {round(area, 3)} square units")
except ValueError:
    print("Input is not a valid number")

# output: Enter a valid base value: 45.6
#         Enter a valid height value: 89.345
#         Area of the given triangle is 2037.066 square units

# ----------------------------------------------------------------------


# Q3. Calculate the area of a rectangle.

def calcArea(len, brd):
    return len * brd

try:
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))

    area = calcArea(length, breadth)
    print(f"Area of the given rectangle is {round(area, 3)} square units.")
except ValueError:
    print("Input is not a valid number")

# output: Enter the length: 45.67
#         Enter the breadth: 23.987
#         Area of the given rectangle is 1095.486 square units.

# ----------------------------------------------------------------------


# Q4.  Calculate the area of a square.

def calcArea(side):
    return side ** 2

try:
    side = float(input("Enter the side length: "))

    area = calcArea(side)
    print(f"Area of the given square is {round(area, 3)} sq units.")
except ValueError:
    print("Input is not a valid number")

# output : Enter the side length: 97.635
#          Area of the given square is 9532.593 sq units.









