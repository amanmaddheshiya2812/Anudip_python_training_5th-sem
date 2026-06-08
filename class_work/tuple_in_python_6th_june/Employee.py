"""wap to create a dict that contains the record of 10 employee where employee id used as I key and salary is used as value. find out the total
no of employee having salary gtr then 30000
display the list of employee whose salary is below 20000"""
# Create a dictionary of 10 employees
employees = {
    101: 25000,
    102: 35000,
    103: 18000,
    104: 42000,
    105: 15000,
    106: 32000,
    107: 28000,
    108: 50000,
    109: 19000,
    110: 38000
}

# Find total number of employees having salary greater than 30000
count = 0
for salary in employees.values():
    if salary > 30000:
        count += 1

print("Total employees with salary greater than 30000 =", count)

# Display employees whose salary is below 20000
print("\nEmployees having salary below 20000:")
for emp_id, salary in employees.items():
    if salary < 20000:
        print("Employee ID:", emp_id, "Salary:", salary)