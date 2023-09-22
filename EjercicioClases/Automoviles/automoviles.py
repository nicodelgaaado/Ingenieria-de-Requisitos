class Customer:
    def __init__(self, unique_code, name, address, telephone):
        self.unique_code = unique_code
        self.name = name
        self.address = address
        self.telephone = telephone
        self.endorsed_by = None  # Initially, no endorsement

    def endorse(self, customer):
        self.endorsed_by = customer

class Car:
    def __init__(self, license_plate, model, color, make, garage):
        self.license_plate = license_plate
        self.model = model
        self.color = color
        self.make = make
        self.garage = garage

class Reservation:
    def __init__(self, customer, cars, start_date, end_date, rental_price, fuel_liters, delivered, agency):
        self.customer = customer
        self.cars = cars
        self.start_date = start_date
        self.end_date = end_date
        self.rental_price = rental_price
        self.fuel_liters = fuel_liters
        self.delivered = delivered
        self.agency = agency

    def calculate_total_price(self):
        return sum(car.rental_price for car in self.cars)

# Sample data for testing
customers = []
cars = []
reservations = []

import random
import string

# Function to generate a random unique code
def generate_unique_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

def create_customer():
    unique_code = generate_unique_code()
    name = input("Enter customer's name: ")
    address = input("Enter customer's address: ")
    telephone = input("Enter customer's telephone number: ")
    customer = Customer(unique_code, name, address, telephone)
    customers.append(customer)
    print(f"Customer registered with unique code: {unique_code}")

def create_car():
    license_plate = input("Enter car's license plate number: ")
    model = input("Enter car's model: ")
    color = input("Enter car's color: ")
    make = input("Enter car's make: ")
    garage = input("Enter garage assigned to the car: ")
    car = Car(license_plate, model, color, make, garage)
    cars.append(car)

def create_reservation():
    unique_code = input("Enter customer's unique code for the reservation: ")
    customer = next((c for c in customers if c.unique_code == unique_code), None)
    if customer is None:
        print("Customer not found.")
        return

    car_count = int(input("Enter the number of cars for this reservation: "))
    cars_for_reservation = []
    for i in range(car_count):
        license_plate = input(f"Enter license plate for car {i + 1}: ")
        car = next((c for c in cars if c.license_plate == license_plate), None)
        if car is None:
            print(f"Car with license plate {license_plate} not found.")
            return
        cars_for_reservation.append(car)

    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    rental_price = float(input("Enter rental price per car: "))
    fuel_liters = float(input("Enter liters of fuel in the tank at booking: "))
    delivered = input("Has the car(s) been delivered? (yes/no): ").lower() == "yes"
    agency = input("Enter the agency for the reservation: ")

    reservation = Reservation(customer, cars_for_reservation, start_date, end_date, rental_price, fuel_liters, delivered, agency)
    reservations.append(reservation)

def main():
    while True:
        print("\nCar Rental Company Management System")
        print("1. Create Customer")
        print("2. Create Car")
        print("3. Create Reservation")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_car()
        elif choice == "3":
            create_reservation()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
