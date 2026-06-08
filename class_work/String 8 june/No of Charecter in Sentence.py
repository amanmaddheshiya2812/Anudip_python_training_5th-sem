#WAP to input a string or a sentence from user and count the number of characters in the sentence and count the number of special characters in the sentence
string = input("Enter a string or sentence: ")
char_count = len(string)
special_count = 0
for char in string:
    if char in "!@#$%^&*( )_+-=[]{}|;':\",.<>?/":
        special_count += 1
print("Number of characters:", char_count)
print("Number of special characters:", special_count)