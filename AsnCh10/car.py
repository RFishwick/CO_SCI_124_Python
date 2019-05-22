# Car class
# The Car class provide access to a car's data,
# and provides acceleration and deceleration methods

class Car:	
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Define set / mutator methods
    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = speed

    # Define get / accessor methods
    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    # Define acceleration and deceleration methods
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5


# The main function.
def main():
    print("\nA Program to define a car and manipulate it's velocity\n")
    year_model = input("Input Year and Model: ")
    make = input("Input Make: ")

    # Create an object from the Car class.
    my_car = Car(year_model, make)

    #  Set initial car speed to 0
    my_car.set_speed(0)

    # Print car attributes
    print("\nCar attributes and initial speed:")
    print("Year and Model: ", my_car.get_year_model())
    print("Make: ", my_car.get_make())
    print_speed(my_car.get_speed())

    #  Accelerate 5 times
    print("\nAccelerate")
    for i in range(5):
        my_car.accelerate()
        print_speed(my_car.get_speed())

    # Decelerate 5 times
    print("\nBrake")
    for i in range(5):
        my_car.brake()
        print_speed(my_car.get_speed())


# Function to print formatted speed
def print_speed(speed):
    print("Speed: ", speed)


# Call the main function.
main()
