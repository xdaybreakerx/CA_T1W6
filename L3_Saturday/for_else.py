# for else

# for .. in ..:
#   loop statements
# else:
#   else statements

# else statement is executed when the loop successfully finishes
# but is not executed when the loop breaks

for i in range (0, 10):
    print(i)
    if i == 11:
        break
else:
    print("Loop finished")
    
num = 23
for i in range(2, num):
    if (num % i == 0): 
        print("Not a prime")
        break
    else:
        print("A prime")