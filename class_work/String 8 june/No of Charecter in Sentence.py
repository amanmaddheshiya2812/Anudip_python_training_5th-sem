#WAP to input a string or a sentence from user and count the number of characters in the sentence and count the number of special characters in the sentence without using any built in function using len() function.
string = input("Enter a string or sentence: ")
char_count = 0
special_char_count = 0
for char in string:
    char_count += 1
    if not char.isalnum() :
        special_char_count += 1
print("Number of characters:", char_count)