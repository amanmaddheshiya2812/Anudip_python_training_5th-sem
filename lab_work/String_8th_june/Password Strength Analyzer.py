'''Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. 
Rules: 
• Minimum length 8  
• Contains at least:  
o 1 uppercase letter  
o 1 lowercase letter  
o 1 digit  
o 1 special character  
Additionally: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Display all digits separately.  
6. Display all special characters separately. '''

password = input("Enter a password: ")

# Initialize counters and lists
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

digits_found = []
specials_found = []

# Process the password
for char in password:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
        digits_found.append(char)
    else:
        # Assuming any other character is a special character
        special_count += 1
        specials_found.append(char)

# Determine Strength
# Strong: Min length 8 AND has at least one of each category
is_strong = (len(password) >= 8 and upper_count > 0 and 
             lower_count > 0 and digit_count > 0 and special_count > 0)

# Medium: Length is 8 but missing a category, or shorter but contains variety
is_medium = len(password) >= 6

if is_strong:
    strength = "Strong"
elif is_medium:
    strength = "Medium"
else:
    strength = "Weak"

# Display Results
print(f"\nPassword: {password}")
print(f"\nUppercase Letters: {upper_count}")
print(f"Lowercase Letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Special Characters: {special_count}")
print(f"\nDigits Found: {digits_found}")
print(f"Special Characters Found: {specials_found}")
print(f"\nPassword Strength: {strength}")