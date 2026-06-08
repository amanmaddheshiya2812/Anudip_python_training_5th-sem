performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}
#----------------------------------------------
# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp)
#----------------------------------------------
# 2. Count employees needing improvement (score < 60)
needing_improvement = [emp for emp, score in performance.items() if score < 60]
print(f"\nEmployees Needing Improvement: {len(needing_improvement)}")
#-----------------------------------------------
# 3. Find the top performer
top_emp = max(performance, key=performance.get)
print(f"Top Performer: {top_emp} ({performance[top_emp]})")
#-----------------------------------------------
# 4. Calculate average performance score
avg_score = sum(performance.values()) / len(performance)
print(f"Average Score: {avg_score}")
#------------------------------------------------
# 5. Create separate lists based on categories
excellent = []
good = []
average = []
poor = []
#------------------------------------------------
for emp, score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif 75 <= score <= 89:
        good.append(emp)
    elif 60 <= score <= 74:
        average.append(emp)
    else:
        poor.append(emp)

print(f"\nExcellent: {excellent}")
print(f"Good: {good}")
print(f"Average: {average}")
print(f"Poor: {poor}")