# check whether a string is a palindrome or not

# string reversed is the same as original string 

# eg 
# simon = nomis # not a palindrome
# anna = anna # a palindrome 

original_string = "racecar"

reversed_string = ""

for character in original_string:
    reversed_string = character + reversed_string
    
print(reversed_string)

# or
# string[start:end:step]

print(original_string[::-1])

if(original_string[::-1] == original_string):
    print("Palindrome")
else:
    print("not palindrome")
    
print("palindrome") if (original_string[::-1] == original_string) else print("not palindrome")

print(original_string[::-1] == original_string)