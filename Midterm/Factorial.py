# Factorial
# Calculate the factorial for a non negative integer number

# Define initial factorial result as 1
result = 1

# Get a non negative integer number
number = int(input("Enter the number: ")) + 1

# Loop through a range of numbers from 1 to number
for i in range(1, number):
    result = result * i  # Replace result with current value of result * i

print("Factorial:", format(result, ','))  # Print factorial result

