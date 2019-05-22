#  Program to use ShiftSupervisor Object

import emp


def main():
    # Local variables
    supervisor_name = ''
    supervisor_id = ''
    supervisor_salary = 0.0
    supervisor_bonus = 0.0

    # Get data attributes
    supervisor_name = input('\nEnter the name: ')
    supervisor_id = input('Enter the ID number: ')
    supervisor_salary = int(input('Enter the annual salary: $'))
    supervisor_bonus = float(input('Enter the annual bonus rate: $'))

    # Create an instance of ShiftSupervisor
    supervisor = emp.ShiftSupervisor(supervisor_name, supervisor_id, \
                                     supervisor_salary, supervisor_bonus)

    # Display information
    print('\nShift supervisor information:')
    print('Name:', supervisor.get_name())
    print('ID number:', supervisor.get_id_number())
    print('Annual salary: $', format(supervisor.get_annual_salary(), ',.2f'), sep='')
    print('Annual bonus: $', \
          format(supervisor.get_annual_bonus(), ',.2f'), sep='')


# Call the main function.
main()
