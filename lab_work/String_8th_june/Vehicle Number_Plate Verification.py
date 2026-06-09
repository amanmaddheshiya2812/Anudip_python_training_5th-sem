'''Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
o First 2 characters must be alphabets.  
o Next 2 must be digits.  
o Next 2 must be alphabets.  
o Last 4 must be digits.  
7. Display whether the number plate is valid. '''

plate = "MH12AB4589"

# 1-4. Extracting components
state_code = plate[0:2]
district_code = plate[2:4]
series = plate[4:6]
vehicle_num = plate[6:10]

# 5. Count letters and digits
letters = sum(c.isalpha() for c in plate)
digits = sum(c.isdigit() for c in plate)

# 6. Verification checks
is_valid = (
    state_code.isalpha() and 
    district_code.isdigit() and 
    series.isalpha() and 
    vehicle_num.isdigit() and
    len(plate) == 10
)
# 7. Display Results
print(f"Vehicle Number: {plate}")
print(f"State Code: {state_code}")
print(f"District Code: {district_code}")
print(f"Series: {series}")
print(f"Vehicle Number: {vehicle_num}")
print(f"\nTotal Letters: {letters}")
print(f"Total Digits: {digits}")
print(f"\nVehicle Number Status: {'Valid' if is_valid else 'Invalid'}")