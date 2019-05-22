#  Module emp

#  The Employee class represents a generic employee
class Employee:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number


#  The ProductionWorker class is a subclass of the Employee class
class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift_number, pay_rate):
        # Call superclass __init__ method.
        Employee.__init__(self, name, id_number)

        # Initialize the shift_number and pay_rate attributes.
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    # Mutator functions for shift_number and pay_rate.
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    # Accessor functions for shift_number and pay_rate.
    def get_shift_number(self):
        return self.__shift_number


def get_pay_rate(self):
    return self.__pay_rate


#  The ShiftSupervisor class is a subclass of the Employee class
class ShiftSupervisor(Employee):
    def __init__(self, name, id_number, annual_salary, annual_bonus):
        # Call superclass __init__ method.
        Employee.__init__(self, name, id_number)

        # Initialize the annual_salary and annual_bonus attributes.
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    # Mutator functions for annual_salary and annual_bonus.
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    # Accessor functions for annual_salary and annual_bonus.
    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus
