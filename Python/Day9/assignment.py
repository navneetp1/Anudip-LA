# Q1. Write a Python program to Count all letters, digits, and special symbols from the given string
# Input = “P@#yn26at^&i5ve” 

# text = input("Enter some text: ")
# length = len(text)
# letters = 0
# digits = 0
# symbols = 0
# for i in range(length):
#     if text[i].isalpha():
#         letters+=1
#     elif text[i].isdigit():
#         digits+=1
#     else:
#         symbols+=1

# print(f"The given input string {text} contains \n{letters} letters, \n{digits} digits and \n{symbols} symbols.")


#  Q2. Write a Python program to remove duplicate characters of a given string.
#  Input = “String and String Function” 

# text = input("Enter some text: ")
# text = text.lower()
# word=""
# for i in text:
#     if i not in word:
#         word+=i   
# print("Given string with no duplicates\n", word)


# Q3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
# Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 

# textInput = input("Enter some text: ")
# length = len(textInput)
# uppercase = 0
# lowercase = 0
# special = 0
# numeric = 0

# for i in range(length):
#     if textInput[i].isupper():
#         uppercase+=1
#     elif textInput[i].islower():
#         lowercase+=1
#     elif textInput[i].isdigit():
#         numeric+=1
#     else:
#         special+=1

# print(f"The given input has \n{uppercase} Uppercase characters, \n{lowercase} Lowercase characters, \n{numeric} Numeric characters and \n{special} special characters")

# Q4.Write a Python Count vowels in a string 
# Input= “Welcome to Python Assignment”

textInput = input("Enter some text: ")
vowels=0
consonants=0
for i in range(0, len(textInput)):
    if textInput[i].lower() in "aeiou":
        vowels+=1
    else:
        consonants+=1

print("Vowels", vowels)








