# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# ask user to input a string
string = input("Enter a string: ")

# ask user to input a character to find
char = input("Enter a character to find: ")

# initialize the index to -1
index = -1

# loop through the string in reverse order
for i in range(len(string) - 1, -1, -1):
    if string[i] == char:  # check if the character is found
        index = i
        break

# print the result
if index != -1:
    print(f"The first location of '{char}' in the string '{string}' from the last character is: {index}.")