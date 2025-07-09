# Creating and using a custom exception

class InvalidMarkException(Exception):
    pass

def validate_marks(mark):
    if mark < 0 or mark > 100:
        raise InvalidMarkException("❌ Marks must be between 0 and 100.")
    print("✅ Valid marks:", mark)

try:
    validate_marks(int(input("Enter student mark: ")))
except InvalidMarkException as e:
    print("Custom Error:", e)
except ValueError:
    print("❌ Please enter a valid number.")