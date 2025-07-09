# OOP-based calculator
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self): return self.a + self.b
    def subtract(self): return self.a - self.b
    def multiply(self): return self.a * self.b
    def divide(self): return self.a / self.b if self.b != 0 else "Undefined"

# User interaction
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
calc = Calculator(a, b)

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Choose an operation: "))

if choice == 1:
    print("Result:", calc.add())
elif choice == 2:
    print("Result:", calc.subtract())
elif choice == 3:
    print("Result:", calc.multiply())
elif choice == 4:
    print("Result:", calc.divide())
else:
    print("Invalid choice")