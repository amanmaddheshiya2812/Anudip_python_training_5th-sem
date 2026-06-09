'''Tasks 
Write a program to: 
1. Count the number of uppercase letters.  
2. Count the number of digits.  
3. Extract the joining year.  
4. Extract the employee name.  
5. Check whether the ID follows these rules:  
o Starts with "EMP"  
o Contains exactly 4 digits for the year  
o Ends with exactly 3 digits  
6. Create a list containing all digits present in the ID.  
7. Find the sum of all digits present in the ID.  
8. Display whether the ID is valid or invalid. '''

emp_id = "EMP2026ANUJ458"

# 1. & 2. Count uppercase letters and digits
uppercase_count = sum(1 for char in emp_id if char.isupper())
digits = [int(char) for char in emp_id if char.isdigit()]
digit_count = len(digits)

# 3. Extract the joining year (Positions 3-7)
joining_year = emp_id[3:7]

# 4. Extract the employee name
# Assuming name is between the year and the last 3 digits
emp_name = emp_id[7:-3]

# 5. Validation Rules
starts_with_emp = emp_id.startswith("EMP")
has_4_digit_year = joining_year.isdigit() and len(joining_year) == 4
ends_with_3_digits = emp_id[-3:].isdigit()

# 6. & 7. List and Sum of digits
digit_sum = sum(digits)

# 8. Validity Check
is_valid = starts_with_emp and has_4_digit_year and ends_with_3_digits
status = "Valid" if is_valid else "Invalid"

# Display Output
print(f"Employee ID: {emp_id}")
print(f"\nUppercase Letters: {uppercase_count}")
print(f"Digits: {digit_count}")
print(f"\nJoining Year: {joining_year}")
print(f"Employee Name: {emp_name}")
print(f"\nDigit List: {digits}")
print(f"Sum of Digits: {digit_sum}")
print(f"\nID Status: {status}")