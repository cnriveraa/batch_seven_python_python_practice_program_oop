# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# ask user to input a string
string = input("Enter a string: ")

# ask user to input a character to count
char = input("Enter a character to count: ")

# initialize a variable to count the number of times the character appears in the string
count = 0

# loop through each character in the string
for i in string:
    if i == char: # if the character is equal to the character to count, increment the count
        count += 1

# print the count