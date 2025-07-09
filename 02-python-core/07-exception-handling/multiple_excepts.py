# Handling multiple specific exceptions
try:
    lst = [1, 2, 3]
    index = int(input("Enter index: "))
    print("Value:", lst[index])
except IndexError:
    print("❌ Index out of range.")
except ValueError:
    print("❌ Invalid index input.")
except Exception as e:
    print("Something went wrong:", str(e))