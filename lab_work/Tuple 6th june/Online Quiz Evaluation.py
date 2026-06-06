# Problem Data
correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

# Initialize counters and lists
score = 0
incorrect_questions = []
total_questions = len(correct)

# Evaluate answers
for i in range(total_questions):
    if student[i] == correct[i]:
        score += 1
    else:
        # Question numbers typically start at 1
        incorrect_questions.append(i + 1)

# Calculations
wrong_count = total_questions - score
percentage = (score / total_questions) * 100
status = "Pass" if percentage >= 60 else "Fail"

# Display Results
print(f"Total Score: {score}/{total_questions}")
print(f"Incorrectly Answered Question Numbers: {incorrect_questions}")
print(f"Correct Answers: {score}")
print(f"Wrong Answers: {wrong_count}")
print(f"Result: {status} ({percentage}%)")