# Recursive Multiplication


def main():
    # Declare local variable
    x = 0
    y = 0

    # Get numbers as input from the user.
    print('Program to multiply two positive integers using a recursive function')
    x = int(input('Enter the value of X: '))
    y = int(input('Enter the value of Y: '))

    # Display the numbers.
    print('Result: ', multiply_num(x, y))


# multiply_num is a recursive function
# that accepts two positive non zero integer arguments.
# It returns the value of x times y.
def multiply_num(x, y):
    if x == 0:
        return 0
    if x == 1:
        return y

    return y + multiply_num(x - 1, y)  # Recursively increment y by y


# Call the main function.
main()
