# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# ask user to input a string
string = input("Enter a string: ")

# check if all characters are in lowercase
is_lowercase = True

for char in string:
    if char.isalpha() and not ('a' <= char <= 'z'):
        is_lowercase = False
        break

# print the result
if is_lowercase:
    print("All characters are in lowercase.")
else:
    print("Not all characters are in lowercase.")