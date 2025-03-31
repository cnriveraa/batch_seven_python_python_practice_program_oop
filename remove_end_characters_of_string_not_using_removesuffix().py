# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# ask user to enter a string
string = input("Enter a string: ")

# ask user to enter a suffix
suffix = input("Enter a suffx to be removed: ")

# check if the string ends with the suffix
if string.endswith(suffix):
    new_string = string[:len(string) - len(suffix)]  # remove the suffix from the string
else: 
    new_string = string

# print the new string
print("String after removing the suffix:", new_string)