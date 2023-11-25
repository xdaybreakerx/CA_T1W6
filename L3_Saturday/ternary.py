# if the given number is divisible by 3 or 5, print True, else print False

num = int(input("Please enter number: "))

if num == 0:
    print(False)
else: 
    if ((num % 3 == 0) or (num % 5 == 0)):
        print(True)
    else: 
        print(False)

# or:
print(False if num == 0 else True if ((num % 3 == 0) or (num % 5 == 0)) else False) 

# or: 
print(num != 0 and ((num % 3 == 0) or (num % 5 == 0)))