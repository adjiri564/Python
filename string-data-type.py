myString = "This is a string"
print(myString)
print(type(myString))
print(str(myString) + " is of the data type " + str(type(myString)))

# String concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Input String
name = input("What is your name?  ")
print(name)

# Formatting output strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))