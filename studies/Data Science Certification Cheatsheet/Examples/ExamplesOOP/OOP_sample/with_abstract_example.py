class Vehicle():
    """
    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """
    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass


class Car(Vehicle):
    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'


class Truck(Vehicle):
    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'


v1 = Vehicle(1200, "vmake", "vmodel", 2002, 855);
print('Vehicle Sale Price:', v1.sale_price())
print('Vehicle Type:', v1.vehicle_type())

# print('Car Details:')
# c1 = Car(1200, "carMake", "carModel", 2002, None)
# print('Car Sale Price:', c1.sale_price())
# print('Vehicle Type:', c1.vehicle_type())
