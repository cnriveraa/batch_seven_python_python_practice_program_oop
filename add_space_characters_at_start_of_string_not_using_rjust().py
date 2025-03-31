# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# ask user to input a string
string = input("Enter a string: ")

# ask user to input the number of characters
number_of_characters = int(input("Enter the number of characters: "))

# check if the length of the string is less than the number of characters
if len(string) < number_of_characters:
    spaces = number_of_characters - len(string)    # calculate the number of spaces needed
    spaces_string = " " * spaces   # create a string with the number of spaces needed
    new_string = spaces_string + string   # add the spaces to the beginning of the string
else:
    new_string = string

# print the new string
print("Right-justified string:", new_string)