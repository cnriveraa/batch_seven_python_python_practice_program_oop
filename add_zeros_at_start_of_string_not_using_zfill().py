# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# ask user to input a string and a number
string = input("Enter a string: ")
number = int(input("Enter a number: "))

# check if the length of the string is less than the number
if len(string) < number:
    zeros_to_add = number - len(string)  # calculate the number of zeros to add
    string = "0" * zeros_to_add + string   # add zeros at the beginning of the string
    print("String with added zeros:", string)
else:
    print("The length of the string is greater than or equal to the number. No zeros added.")