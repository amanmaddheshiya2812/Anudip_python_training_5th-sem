attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# Count present and absent days
present_days = attendance.count('P')
absent_days = attendance.count('A')
total_days = len(attendance)

# Calculate attendance percentage
percentage = (present_days / total_days) * 100

# Determine eligibility (minimum 75%)
is_eligible = percentage >= 75

# Display positions where the student was absent
# Adding 1 to the index to show human-readable positions (1-15)
absent_positions = [i + 1 for i, status in enumerate(attendance) if status == 'A']

# Display results
print(f"Present Days: {present_days}")
print(f"Absent Days: {absent_days}")
print(f"Attendance Percentage: {percentage:.2f}%")
print(f"Eligibility: {'Eligible' if is_eligible else 'Not Eligible'}")
print(f"Absent Positions: {absent_positions}")