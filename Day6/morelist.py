# 1. WAP to tak a list print all the prime number available in list?
# list = [3,4,5,6,7,8,9]
# Output: 3, 5, 7
prime = []
countPrime = 0
list = [3,4,5,6,7,8,9, 12,34,56,78]
for number in list:
    if number == 2:
        prime.append(number)
        countPrime+=1
    else:
        flag = True
        for i in range(2,number):
            if number % i == 0:
                flag=False
                break

        if flag==True:
            prime.append(number)
            countPrime+=1


print(f"Total primes: {len(prime)}, {prime}")

# 2. WAP to take a list print count of all prime number available in list?
prime = []
countPrime = 0
list = [3,4,5,6,7,8,9, 12,34,56,78]
for number in list:
    if number == 2:
        prime.append(number)
        countPrime+=1
    else:
        flag = True
        for i in range(2,number):
            if number % i == 0:
                flag=False
                break

        if flag==True:
            prime.append(number)
            countPrime+=1


print(f"Total primes: {len(prime)}, {countPrime}")

# 3. WAP to take a list and print count of all even and odd numbers available in list?
# list = [3,4,5,6,7,8,9, 12,34,56,78]
# even = 0
# odd = 0

# for i in range(len(list)):
#     if(list[i] % 2 == 0):
#         even+=1
#     else:
#         odd+=1

# print(f"No of even numbers: {even}; No of odd numbers:{odd}")