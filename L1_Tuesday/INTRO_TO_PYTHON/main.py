print("Hello World!")

print("Second print statement")

print("Third print statement")

# is for commenting in Python

# Data Types:

# Numbers:
# int eg, 5, 100, 10000
print(type(5))

# float eg, 2.5, -1.6, 100.3
print (type(5.3))

# complex eg, 2 + 3j (j for imaginary numbers not i)
print(type(5 - 6j))

# Operations in Numbers
print (2 + 3)
print (2 - 5)
print(2 * 5)
print(2 / 5) # py will convert an int to float at output during division
print(2 % 5) # yields the remainder when the first operand is divided by the second

# Strings
"Python supports Double Quotations"
'Python also supports Single Quotations'
print(type("Hello World!"))

# String concatenation - addition / join
print ("Hello" + " World!")

# String Methods 
print("Hello".upper())
print("Hello".lower())

# Boolean eg, True or False
print(type(True))

# Falsy values
False
0 
None
[] # empty list
() # empty tuple
{} # empty set
# eg
print(bool(0))
print(bool(""))

# Truthy values
True 
2, 5.3, -7 # any number other than 0
"a", "hello" # any string that is not empty
# any list, tuple, or set with any item eg
[1]
(1)
{1}
#eg
print(bool(1))
print(bool("a"))

# Comparison Operators (>, <, >=, <=, ==) (outputs boolean values)
print(2 > 3) # outputs true
print(2 < 3) # outputs false
print(5 > 5) # outputs false
print(5 >= 5) # outputs true
print(5 == 5) # outputs true

# Logical Operators (and, or, not)
# eg

# Truth table:

#  First Operator   Second Operator     and result      or result
#  true             true                true            true                
#  true             false               false           true           
#  false            true                false           true           
#  false            false               false           false           

#   expression      not result
#   true            false
#   false           true

# Eg,
print(True and False)
print (True or False)
print(not False)

# Or can also use truthy/falsy values
print("" and "a")
print(1 or 0)
print(not 0)

# Variables
# Comparison statement set:
print(2 + 3)
print(2 - 3)
print(2 * 3)

num1 = 5
num2 = 3
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)

# or 

num1 = 5
num2 = 30
print(num1 + num2)
print(num1 - num2)

num2 = 10
print(num1 * num2)

# String interpolation with variables
print("My name is John and I live in Australia")

# or
name = "John"
country = "Australia"
print("My name is " + name + " and I live in " + country) 

# or 
print(f"My name is {name} and I live in {country}")

