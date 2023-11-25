# Primitive Data Type - can hold a single piece of data
# Numbers (int, float), String, Boolean
# eg
# a = 501
# a = "String"
# a = True

# Complex Data Types - can hold multiple pieces of data
# List - (Array) - collection of data - mutable  - indexed

# numbers = [ 15, 2, 23, 98, 56 ]
# # index     0   1  2   3   4    ...     ...     ...

# print(numbers)
# # will print all numbers in list (15, 2, 23, 98, 56)
# print(numbers[2])
# # will print the number in the second index
# numbers[2] = 10
# # change number at index to new value
# print(numbers)
# # will print all numbers in list (15, 2, 10, 98, 56)
# print(len(numbers))
# # prints 5 - the length of the list
# numbers.append(42)
# # appends 42 to end of list
# print(numbers)
# # prints all numbers with 42 added to end
# numbers.insert(2, 72)
# # inserts at specified index, then value 
# print(numbers)
# # prints all numbers with 72 added before 10 
# numbers.pop()
# # removes the last value in the list
# print(numbers)
# # shows this change - 56 removed
# numbers.remove(98)
# # removes specific value in list
# print(numbers)
# # shows this change - 98 removed
# numbers.pop(3)
# # remove at specified index, else defaults to last
# numbers.sort()
# # sorts list
# print(numbers)
# numbers.reverse()
# # reverses list
# print(numbers)

# new_numbers = [ 13, 45, 62, 13, 45, 13 ]
# print(new_numbers.count(13))
# # how many times does this number occur
# print(new_numbers.index(62))
# # what index is the number at in the array
# print(new_numbers.index(45))
# # specifically this shows only the first time the number occurs
# print(numbers + new_numbers)
# # concats both 

# Tuples - similar to list - collection of data - indexed - immutable

names = ( "John", "Jane", "Mike" )
# index    0       1       2
print(names)
print(type(names))

# eg names.append() - would result in error as Tuple is immutable

print(names.count("John"))
print(names.index("Mike"))
print(len(names))
print(names(2))

# Use cases:
# eg
# days_of_the_week = ( "Monday", "Tuesday", "Wednesday", ..., ..., )
# month = ( "January", "February", "March", ..., ...,)

# Simple data types copy by value 
# Complex data types copy by references 
