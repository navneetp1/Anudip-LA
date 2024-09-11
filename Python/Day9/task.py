stored_usernames = ["abctest"]
stored_password = ["strongpassword234"]

def passwordAttempts(user):
    attempt = 3
    while(attempt):
        password = input("Password: ")
        if password in stored_password:
            print(f"Hi {user}, Welcome to the Bank Dashboard.")
            return
        else:
            attempt -= 1
            if attempt > 0:
                print(f"Wrong password!, You are left with {attempt} attempts until temporary softlock.")

    print("Login later.. you used all your password attempts")

print("Login | SignUp")
user = input("Username: ")


if user in stored_usernames:
    passwordAttempts(user)
else:
    print("Username not found, try again")












# if givenusername == storedusername:
#     passwordadd()
# else
#     username not found

# passwordadd():
# attempts = 3
# input
# while(attempts):
#     if(input == storedpassword)
#         welcome to bank
#     else:
#         attempts -= 1
#         please try again. {attempts} left


# print(all attempts exhausted)


