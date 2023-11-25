# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# number = 1

# while number <= 6:
#     print(number)
#     number += 1
    
login_attempts = 5

while login_attempts > 0: 
    password = input("Enter password: ")
    if (password != "hello"):
        print("Wrong password")
        login_attempts -= 1
        print(f"Remaining attempts: {login_attempts}")
    else:
        print("Password correct")
        break