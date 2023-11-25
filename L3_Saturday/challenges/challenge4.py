# calculate factorial 

# eg
# 6! = 6 * 5 * 4 * 3 * 2 * 1

num = 10

factorial_value = 1

for i in range (1, num+1):
    factorial_value *= i
    
print(factorial_value)