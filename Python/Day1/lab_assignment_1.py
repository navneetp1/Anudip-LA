#Q.1 print helloworld

print("hello world")

# output : hello world

# ---------------------------------------------------------------------

#Q.2 describe local variable and global variable code

glob = 40
def localCall():
    local = 30
    print(f"This variable local = {local} is in local scope")

print(glob)
localCall()
# print(local) # you can't access this even if you try

# output : 40
        #  This variable local = 30 is in local scope

# ----------------------------------------------------------------------


# Q.3 Write a code that describe Indentation error

# def hello():
# print("Hello") # this line here is not intended properly due to which it gives an indentation error

# hello()

# ----------------------------------------------------------------------


# Q.4 write a code that describe local and global variable with same name
num=10
def printNum():
    num = 20
    print(f"number is {num}")

print(num)
printNum()

# output: 10
        # number is 20


# ----------------------------------------------------------------------


# Q.5 Write a code for string, int and float input.

string_input = input("Enter string: ")
int_input = int(input("Enter integer: "))
float_input = float(input("Enter integer: "))

print(f"{string_input}      {int_input}     {float_input}")


#           hello
#           4
#           4.3
#  output:  hello     4       4.3

# ----------------------------------------------------------------------


