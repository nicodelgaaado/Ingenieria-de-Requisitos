class Employee:
    def __init__(self, name, age, gross_salary, is_manager=False):
        self.name = name
        self.age = age
        self.gross_salary = gross_salary
        self.is_manager = is_manager
        self.subordinates = []

    def add_subordinate(self, subordinate):
        if self.is_manager:
            self.subordinates.append(subordinate)
        else:
            print(f"{self.name} is not a manager!")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gross Salary: ${self.gross_salary}")
        if self.is_manager:
            print("Category: Manager")
            print(f"Number of Subordinates: {len(self.subordinates)}")
            if len(self.subordinates) > 0:
                print("Subordinates:")
                for subordinate in self.subordinates:
                    print(f"- {subordinate.name}")
        else:
            print("Category: Employee")

class Customer:
    def __init__(self, name, age, contact_phone):
        self.name = name
        self.age = age
        self.contact_phone = contact_phone

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Contact Phone: {self.contact_phone}")


def main():
    companies = []

    while True:
        print("\nCompany Management System")
        print("1. Create Company")
        print("2. Add Employee")
        print("3. Add Manager")
        print("4. Add Customer")
        print("5. Show Company Data")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            company_name = input("Enter the company name: ")
            company = {
                "name": company_name,
                "employees": [],
                "managers": [],
                "customers": [],
            }
            companies.append(company)
            print(f"{company_name} has been created.")

        elif choice == "2":
            company_name = input("Enter the company name: ")
            employee_name = input("Enter the employee name: ")
            age = int(input("Enter the employee age: "))
            gross_salary = float(input("Enter the employee's gross salary: "))
            is_manager = False

            for company in companies:
                if company["name"] == company_name:
                    employee = Employee(employee_name, age, gross_salary, is_manager)
                    company["employees"].append(employee)
                    print(f"{employee_name} has been added as an employee to {company_name}.")

        elif choice == "3":
            company_name = input("Enter the company name: ")
            manager_name = input("Enter the manager name: ")
            age = int(input("Enter the manager age: "))
            gross_salary = float(input("Enter the manager's gross salary: "))
            is_manager = True

            for company in companies:
                if company["name"] == company_name:
                    manager = Employee(manager_name, age, gross_salary, is_manager)
                    company["managers"].append(manager)
                    print(f"{manager_name} has been added as a manager to {company_name}.")

        elif choice == "4":
            customer_name = input("Enter the customer name: ")
            age = int(input("Enter the customer age: "))
            contact_phone = input("Enter the customer's contact phone number: ")

            for company in companies:
                company["customers"].append(Customer(customer_name, age, contact_phone))
                print(f"{customer_name} has been added as a customer.")

        elif choice == "5":
            company_name = input("Enter the company name: ")

            for company in companies:
                if company["name"] == company_name:
                    print(f"Company Name: {company['name']}")
                    print("Employees:")
                    for employee in company["employees"]:
                        employee.display_info()
                    print("Managers:")
                    for manager in company["managers"]:
                        manager.display_info()
                    print("Customers:")
                    for customer in company["customers"]:
                        customer.display_info()

        elif choice == "6":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
