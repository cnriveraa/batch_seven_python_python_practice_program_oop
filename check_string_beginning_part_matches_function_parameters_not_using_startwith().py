# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# ask user to input a string
string = input("Enter a string: ")

# ask user to input a prefix
prefix = input("Enter a prefix: ")

# check if the string starts with the prefix
if string.find(prefix) == 0:
    print(f"{string} starts with {prefix}.")
else: 
    print(f"{string} does not start with {prefix}.")