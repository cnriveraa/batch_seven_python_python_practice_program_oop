# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# ask user to input a string
string = input("Enter a string: ")

# ask user to input a character to find its first location in the string
char = input("Enter a character to find its first location in the string: ")

# initialize a variable to store the first location of the character in the string
first_location = -1

# loop through the string to find the first location of the character
for i in range(len(string)):
    if string[i] == char:   # check if the character is found in the string
        first_location = i  # if found, store the location and break the loop
        break

# check if the character was found in the string
if first_location != -1:
    print(f"The first location of '{char}' in the string is: {first_location}.")