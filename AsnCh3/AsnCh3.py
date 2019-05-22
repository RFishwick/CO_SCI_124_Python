# Write a program that asks the user to enter the number of packages purchased.
# The program should then display the amount of the discount (if any)
# and the total amount of the purchase after the discount.

# Named constants
UNIT_COST = 99.00

# Variables
qty = 0                 # Package qty (integer)
discount_percent = 0.0  # Default discount percent to 0%
price = 0.0             # qty * UNIT_COST
net_price = 0.0         # price - discount amount

# Get the quantity from the user and convert to int
qty = int(input('Enter package quantity: '))

# Calculate discount
if qty < 10:
    print('Discount: 0%')
    discount_percent = 0.0
elif qty >= 10 and qty < 20:
    print('Discount: 10%')
    discount_percent = 0.1
elif qty >= 20 and qty < 50:
    print('Discount: 20%')
    discount_percent = 0.2
elif qty >= 50 and qty < 100:
    print('Discount: 30%')
    discount_percent = 0.3
else:
    print('Discount: 40%')
    discount_percent = 0.4

# Calculate the price
price = qty * UNIT_COST

# Calculate the net price after discount
net_price = price - (price * discount_percent)

# Print the net price
print('Total purchase price: $', format(net_price, ',.2f'))
