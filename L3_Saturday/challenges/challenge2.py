# count the number of capital letters


sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

vowels = ( "a", "e", "i", "o", "u" )

count_of_vowels = 0
count_of_consonants = 0
count_of_capitals = 0

for character in sentence:
    
    if (character.isupper()):
        count_of_capitals += 1

print(count_of_capitals)

        
