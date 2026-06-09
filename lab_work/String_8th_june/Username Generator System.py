'''Tasks 
Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics. '''
# Input collection and data validation
name = input("Enter your full name: ").strip()

while not name:
    print("Invalid input. Name cannot be empty.")
    name = input("Enter your full name: ").strip()

# 1. Remove spaces & 2. Convert to lowercase
clean_name = name.replace(" ", "").lower()

# 3. Append current year (2026)
raw_username = clean_name + "2026"

# 4. If length exceeds 12, keep only first 12 characters
if len(raw_username) > 12:
    final_username = raw_username[:12]
else:
    final_username = raw_username

# 5. & 6. Count vowels and consonants
vowels_list = "aeiou"
consonants_list = "bcdfghjklmnpqrstvwxyz"
v_count = 0
c_count = 0

for char in final_username:
    if char in vowels_list:
        v_count += 1
    elif char in consonants_list:
        c_count += 1

# 7. Display username statistics
print(f"\nOriginal Name: {name}")
print(f"Generated Username: {final_username}")
print(f"Username Length: {len(final_username)}")
print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")
print("Status: Username Generated Successfully")