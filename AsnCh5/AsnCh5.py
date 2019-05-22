# Paint Job Estimator 
# A painting company has determined that for every 112 square feet of wall space,
# one gallon of paint and eight hours of labor will be required.
# The company charges $35.00 per hour for labor.
#
# Write a program that asks the user to enter the square feet
# of wall space to be painted and the price of the paint per gallon.
#
# The program should display the following data:
# The number of gallons of paint required
# The hours of labor required
# The cost of the paint
# The labor charge
# The total cost of the paint job

# Global constants
FEET_PER_GALLON = 112
HRS_PER_GALLON = 8
HR_RATE = 35.00


# main module
def main():
    # Local variables
    square_feet = 0.0
    price_per_gal = 0.0

    square_feet = float(input('Enter square feet to paint: '))
    price_per_gal = float(input("Enter paint price per gallon: "))

    calc_n_display(square_feet, price_per_gal)


def calc_n_display(sq_ft, pr_per_gal):
    # Local variables
    gallons_rqd = 0.0
    labor_hrs = 0.0
    paint_cost = 0.0
    labor_cost = 0.0
    total_cost = 0.0

    gallons_rqd = sq_ft / FEET_PER_GALLON
    labor_hrs = gallons_rqd * HRS_PER_GALLON
    paint_cost = gallons_rqd * pr_per_gal
    labor_cost = labor_hrs * HR_RATE
    total_cost = labor_cost + paint_cost

    print("\nPaint gallons required:", format(gallons_rqd, ',.2f'))
    print("Labor hours:", format(labor_hrs, ',.2f'))
    print("Paint cost: $", format(paint_cost, ',.2f'), sep='')
    print("Labor cost: $", format(labor_cost, ',.2f'), sep='')
    print("Total cost: $", format(total_cost, ',.2f'), sep='')


# Call the main function.
main()

