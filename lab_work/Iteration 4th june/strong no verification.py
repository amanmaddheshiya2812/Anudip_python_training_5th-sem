# input from the user
num = int(input("Enter a number: "))
temp = num
total_sum = 0
# Extract each digit
while temp > 0:
    digit = temp % 10
    # Calculate factorial of the digit
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    # Add the factorial to the total sum
    total_sum += factorial
    temp //= 10
# Check if the sum matches the original number
if total_sum == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")