# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# ask user to input a string
string = input("Enter a string: ")

# remove space at end of string
result = ' '.join(string.split())

# print the result