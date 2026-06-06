employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Display employees earning above ₹50,000
print("Employees earning above ₹50,000:" )
for name, salary in employees:
    if salary > 50000:
        print(f"- {name}")

# Find the highest-paid employee
highest_paid = max(employees, key=lambda x: x[1])
print(f"\nHighest-paid employee: {highest_paid[0]} (₹{highest_paid[1]})")

# Calculate total salary expenditure
total_expenditure = sum(salary for name, salary in employees)
print(f"Total salary expenditure: ₹{total_expenditure}")

# Count employees earning below ₹40,000
count_below_40k = sum(1 for name, salary in employees if salary < 40000)
print(f"Number of employees earning below ₹40,000: {count_below_40k}")
