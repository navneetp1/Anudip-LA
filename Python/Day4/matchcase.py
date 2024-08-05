# def weekPrint(day):
#     match day:
#         case 1:
#             print("It's a Sunday")
#         case 2:
#             print("It's a Monday")
#         case 3:
#             print("It's a Tuesday")
#         case 4:
#             print("It's a Wednesday")
#         case 5: 
#             print("It's a Thursday")
#         case 6:
#             print("It's a Friday")
#         case 7:
#             print("It's a Saturday")
#         case _:
#             print("Invalid day")

# def monthPrint(month):
#     match month:
#         case 1:
#             print("Month of January")
#         case 2:
#             print("Month of February")
#         case 3:
#             print("Month of March")
#         case 4:
#             print("Month of April")
#         case 5: 
#             print("Month of May")
#         case 6:
#             print("Month of June")
#         case 7:
#             print("Month of July")
#         case 8:
#             print("Month of August")
#         case 9:
#             print("Month of September")
#         case 10:
#             print("Month of October")
#         case 11:
#             print("Month of November")
#         case 12:
#             print("Month of December")
#         case _:
#             print("Invalid input")


# dayNum = int(input("Enter a number for a weekday(1-7): "))
# monthNum = int(input("Enter a number for a month(1-12): "))
# weekPrint(dayNum)
# monthPrint(monthNum)


# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     return fib(n-1)+fib(n-2)

# for i in range(10):
#     print(fib(i), end=' ')


# n=int(input("Number of terms: "))
# i=0
# j=1
# print(i,j, end =" ")
# for k in range(2,n):
#   k = i+j
#   print(k, end = " ")
#   i=j
#   j=k


# for i in range(100,1,-2):
#     print(i, end=" ")



# table = float(input("number daaliye: "))
# for i in range(1,11):
#     print(f"{table} X {i} = {float(table*i)}")


# n = int(input("Enter a number: "))

# for i in range(1,n+1):
#     for j in range(1,i):
#         print(j, end=' ')
#     print(i)


# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(j, end=' ')
#     print()



# for i in range(1,3):
#     for j in range(1, i+2):
#         print(j, end=" ")
#     print()



# 3 
# 3 5
# for i in range(2):
#     for j in range(i+2):
#         print(3+2*j, end=" ")
#     print()



# ---------------------------------------------------------------------------------------
# odd=0
# even=0
# oddCount=0
# evenCount=0

# for i in range(1,11):
#     if(i%2==0):
#         print(f"{i} is even")
#         even += i
#         evenCount+=1
#     else:
#         print(f"{i} is odd")
#         odd += i
#         oddCount+=1

# print(f"Total even sum= {even}, count of even nos = {evenCount}")
# print(f"Total odd sum= {odd}, count of odd nos = {oddCount}")


# for x in range(3, 1, -1):
#     for y in range(4, x+4):
#         print(y,end=' ')
        
#     print()

# for x in range(4, 2, -1):
#     for y in range(4, x+3):
#         print(y,end=' ')
        
#     print()

# for x in range(5, 3, -1):
#     for y in range(4, x+2):
#         print(y,end=' ')
        
#     print()

# for x in range(6, 4, -1):
#     for y in range(4, x+1):
#         print(y,end=' ')
        
#     print()

# for x in range(7, 5, -1):
#     for y in range(4, x):
#         print(y,end=' ')
        
#     print()


# for x in range(12, 3, -2):
#     for y in range(4, x-5):
#         print(y,end=' ')
        
#     print()




    
   




