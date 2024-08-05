try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = int(input("Enter number 3: "))

    if(a==b==c):
        print("All are equal")
    elif (a>=b) and (a>=c):
        if (a==b) or (a==c):
            print(f"{a} is the largest and is equal to one of the other")
        else:
            print(f"{a} is the largest")
    elif (b>=a) and (b>=c):
        if(b==a) or (b==c):
            print(f"{b} is the largest and is equal to one of the other")
        else:
            print(f"{b} is the largest")
    else:
        if(c==a) or (c==b):
            print(f"{c} is the largest and is equal to one of the other")
        else:
            print(f"{c} is the largest")

    # if(a>b):
    #     if(a>c):
    #         print(f"{a} is the largest")
    #     elif(a==c):
    #         print(f"{a} and {c} are equal and largest")
    #     else:
    #         print(f"{c} is the largest")
    # elif(a == b == c):
    #     print(f"All the numbers are equal")
    # elif(a == b):
    #     print(f"{a} and {b} are equal and largest")
    # elif(b==c):
    #     print(f"{b} and {c} are equal and largest")
    # else:    
    #     print(f"{b} is the largest")

    # if a==b==c:
    #     print("All the numbers are equal")
    # elif a>=b and a>=c:
    #     if a==b or a==c:
    #         print(f"{a} is the largest and equal to at least one other number")
    #     else:
    #         print(f"{a} is the largest")
    # elif b>=a and b>=c:
    #     if b==a or b==c:
    #         print(f"{b} is the largest and equal to at least one other number")
    #     else:
    #         print(f"{b} is the largest")
    # else:
    #     if c==a or c==b:
    #         print(f"{c} is the largest and equal to at least one other number")
    #     else:
    #         print(f"{c} is the largest")

except ValueError:
    print("Input is not a valid number")


# left shift me 0 add hote hai right me
# right me 0 minus hota hai right se
# a = 20
# print(bin(a))
# a=a>>2
# print(bin(a), a)