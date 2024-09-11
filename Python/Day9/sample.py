import string
import random
from random import choices
# text = input()

# print(text)
# for i in text:
#     print(i)

# string slicing
name = "0123456789"
length = len(name)
print(name[0:4]) 
print(name[1:4]) 
print(name[1:-3]) 
print(name[-3:-1]) 
print(name[-1:])

# string methods

# newStr = "users navne appdata Local programs.... ....prices ...names"
# print(newStr.upper())
# print(newStr.lower())
# print(newStr.split(" "))
# print(newStr.capitalize())
# print(newStr.replace("navne", "idiot"))

# a = "###??????????"
# print(a.rstrip("?")) 

# str1 = "Hello there..."
# print(str1.endswith("..")) # true
# print(str1.endswith("Hello", 5, 12))
# print(str1.count("e"))


# str2 = "this a solution to the \"is\" problem? "
# print(str2.find("dan"))

name = "hazallingbhum" 
length = len(name)
# new_str = name[1:] + name[0]
# print(new_str)

# new = name[3: length-3] 
# new = new[len(new)-1:] + new[0:len(new)-1]
# print(new)


# r = random.choice(string.ascii_letters)
# print(r.lower())

# word = ''.join(choices(string.ascii_lowercase, k=3))
# print(word)

print(name[::-1])