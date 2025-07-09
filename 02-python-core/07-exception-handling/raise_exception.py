# Raising exceptions manually
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("❌ Cannot divide by zero")
    return a / b

try:
    print("Result:", divide(10, 0))
except ZeroDivisionError as e:
    print("Error:", e)