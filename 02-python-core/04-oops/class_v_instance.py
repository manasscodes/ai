# Class vs Instance Variables
class Employee:
    company = "OpenAI"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.name, "-", e1.company)
print(e2.name, "-", e2.company)

Employee.company = "Google"  # Change class variable
print(e1.name, "-", e1.company)
print(e2.name, "-", e2.company)