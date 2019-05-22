# Sum of Numbers
# Write a program with a loop that asks the user to enter a series of positive numbers.
# The user should enter a negative number to signal the end of the series.
# After all the positive numbers have been entered, the program should display their sum.

# Variables
number = 0
number_sum = 0

while number >= 0:
    number_sum += number  # Increment number_sum by number
    number = int(input("Input number: "))  # Input number

print('Sum: ' + str(number_sum))  # Print final sum
