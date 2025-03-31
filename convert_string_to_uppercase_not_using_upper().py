# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# ask user to input a string
string = input("Enter a string: ")

# create an empty string to store the result
result = ""

# iterate through each character in the string
for char in string:
    if 'a' <= char <= 'z':             # check if the character is a lowercase letter
        result += chr(ord(char) - 32)  # convert it to uppercase by subtracting 32 from its ASCII value
    else:
        result += char    # if not lowercase, keep the character as it is

# print the result