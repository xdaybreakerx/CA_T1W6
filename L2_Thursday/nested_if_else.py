# 2 states - state1 and State2 - take input from user

state = input("Enter your state: ")

# take age from the user

age = int(input("Enter your age: "))

# in state1 
# age >= 18 can vote
# age < 18 cant vote

# in state2 
# age >= 21 can
# age < 21 cant vote

if(state.lower() == "state1"):
    if(age) >= 18:
        print("Can vote in State 1")
    else: 
        print("Can't vote in State 1")
elif(state.lower() == "state2"):
    if(age) >= 21:
        print("Can vote in State 2")
    else: 
        print("Can't vote in State 2")
else: 
    print("Enter a valid state - 'State1', or 'State2'.")