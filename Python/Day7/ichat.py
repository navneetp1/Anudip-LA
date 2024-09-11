# num = 1
# count = 0
# sum = 0

# while count < 100:
#     if num % 2 != 0:  # Check if the number is odd
#         print(num, end=" ")  # Print the odd number
#         sum += num  # Add it to the sum
#         count += 1
#     num += 1
    
#     # Print the sum of the first 100 odd numbers
# print("Sum of the first 100 odd numbers:", sum)


# import random

# def magic_number_game():
#     # Generate a random number between 0 and 20
#     magic_number = random.randint(0, 20)
    
#     # Initialize the guess variable
#     guess = -1  # Set an initial value that can't be correct to start the loop

#     print("Welcome to the Magic Number Guessing Game!")
#     print("I have selected a number between 0 and 20. Can you guess it?")
    
#     # Start the guessing loop
#     while guess != magic_number:
#         try:
#             # Get the player's guess
#             guess = int(input("Enter your guess: "))

#             # Check if the guess is correct
#             if guess == magic_number:
#                 print("Congratulations! You guessed the correct number!")
#             elif guess > magic_number:
#                 print("Wrong guess! Try a smaller number!")
#             else:
#                 print("Wrong guess! Try a larger number.")
        
#         except ValueError:
#             # Handle non-integer inputs
#             print("Invalid input. Please enter a whole number.")

# magic_number_game()

# guests = "Alice Smith<alice@example.com>; Bob Stone<bob@example.com>; Cara Wins<cara@example.com>"

# entries = guests.split("; ")

# for entry in entries:
#     name,email = entry.split("<")
#     email = email.strip(">")
#     print(f"Name: {name}, Email: {email}")

# Debug the following code

# text = "Python is fun!"
# corrected_text = text.replace("Python", "Java")
# print(corrected_text)

# data = "apple,banana,orange,grape,mango"
# # Splitting the string into a list of fruits
# fruits = data.split(",")
# # Slicing to extract the first three fruits
# first_three = fruits[:3]
# # Concatenating the first three fruits into a single string
# first_three_str = "".join(first_three)
# # Printing the results
# print("Original Data:", data)
# print("Fruits List:", fruits)
# print("First Three Fruits:", first_three)
# print("Concatenated First Three Fruits:", first_three_str)
    

names = ["Alice Smith", "Bob Stone", "Cara Wins"]
initials_list = []
for name in names:
    parts = name.split()
    initials = []
    for part in parts:
        initial = part[0].upper()
        initials.append(initial)

    initials_list.append(".".join(initials))


print(initials_list)
    



