'''Tasks 
Write a program to: 
1. Count Present and Absent days.  
2. Calculate attendance percentage.  
3. Find the longest consecutive streak of Presence.  
4. Find the longest consecutive streak of Absence.  
5. Determine whether attendance is below 75%.  '''
attendance = "PPAPPPAAPPPPAPP"

# 1. Count Present and Absent days
present_days = attendance.count('P')
absent_days = attendance.count('A')
total_days = len(attendance)

# 2. Calculate attendance percentage
attendance_percentage = (present_days / total_days) * 100

# 3 & 4. Find longest consecutive streaks
max_p_streak = 0
current_p_streak = 0
max_a_streak = 0
current_a_streak = 0

for char in attendance:
    if char == 'P':
        current_p_streak += 1
        current_a_streak = 0 # Reset absent streak
        if current_p_streak > max_p_streak:
            max_p_streak = current_p_streak
    else: # char == 'A'
        current_a_streak += 1
        current_p_streak = 0 # Reset present streak
        if current_a_streak > max_a_streak:
            max_a_streak = current_a_streak

# 5. Determine if attendance is below 75%
status = "Below 75%" if attendance_percentage < 75 else "75% or Above"

# Output matches sample format
print(f"Attendance Record:\n{attendance}\n")
print(f"Present Days: {present_days}")
print(f"Absent Days: {absent_days}")
print(f"Attendance Percentage: {attendance_percentage:.2f}%")
print(f"\nLongest Present Streak: {max_p_streak}")
print(f"Longest Absent Streak: {max_a_streak}")
print(f"\nAttendance Status: {status}")