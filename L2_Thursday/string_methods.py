# len
# upper
# lower
# split 
# join 
# replace

name = "David Warner"

print(len(name))

print(name.upper())
print(name.lower())

print(name.split("a")) # if no character selected it will split per word

splitted_name = name.split("a")

joined_name = " ".join(splitted_name) # Can use any text in the quotations, eg " ", "-", "hello"

print(joined_name)