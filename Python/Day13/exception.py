def numerical_addition():
    try:
        a = int(input("Enter input 1: "))
        b = input("Enter input 2: ")

        print(f"\n{a+b}")
    except TypeError:
        print("You cannot add a string and an integer, try again")

numerical_addition()