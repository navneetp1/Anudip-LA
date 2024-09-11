
# 1. Print the reverse order series using a while loop

number = int(input("Enter a number: "))
while number:
    print(number, end=" | ")
    number -= 1

    if number == 0:
        print(number, end=" | ")

# 2. Create a code that describe the use of break statement in while loop

attempts = 3
print("What is the capital of USA?")
print("1. London \t\t2. New York")
print("3. Washington D.C \t\t4. Moscow")

while attempts:
    ans = int(input("Enter your choice(1-4): "))
    if ans == 3:
        print("You guessed it right!!")
        break
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left")
        
if attempts == 0:
    print("Correct answer was 3. Washington D.C")

# 3. Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.

str = input("Enter a string: ")
i = 0

while i < len(str):
    print(str[i])
    i += 1

print(f"Length of string {str} is {i}")



# 4.  Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.

num = int(input("Enter input: "))
real = num
fact = 1
while(num > 0):
    fact =  fact * num
    num -= 1

print(f"Factorial of {real} is {fact}") 