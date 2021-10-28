# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method 
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and 
# then call get_range() a second time after upgrading the battery. You should 
# see an increase in the car’s range.

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

def get_descriptive_name(self):
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()

def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")

def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")

def increment_odometer(self, miles):
    self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())