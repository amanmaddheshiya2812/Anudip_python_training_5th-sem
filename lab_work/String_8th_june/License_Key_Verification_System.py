'''Tasks 
Write a program to: 
1. Verify there are exactly 4 groups.  
2. Verify each group contains exactly 4 characters.  
3. Count total letters.  
4. Count vowels.  
5. Remove hyphens and display the merged key.  
6. Create a list containing all groups.  
7. Display whether the key format is valid. '''

license_key = "ABCD-EFGH-IJKL-MNOP"

# 6. Create a list containing all groups
groups = license_key.split('-')

# 1 & 2. Verify groups and lengths
num_groups = len(groups)
all_groups_valid = True

if num_groups != 4:
    all_groups_valid = False
else:
    for group in groups:
        if len(group) != 4:
            all_groups_valid = False

# 3, 4, & 5. Count letters, vowels, and merge key
total_letters = 0
total_vowels = 0
merged_key = ""
vowels = "AEIOUaeiou"

for char in license_key:
    if char != '-':
        merged_key += char
        total_letters += 1
        if char in vowels:
            total_vowels += 1

# 7. Determine status
status = "Valid" if all_groups_valid else "Invalid"

# Display Output
print(f"License Key:\n{license_key}\n")
print(f"Groups:\n{groups}\n")
print(f"Number of Groups: {num_groups}\n")
print(f"Total Letters: {total_letters}")
print(f"Total Vowels: {total_vowels}\n")
print(f"Merged Key:\n{merged_key}\n")
print(f"License Key Status: {status}")