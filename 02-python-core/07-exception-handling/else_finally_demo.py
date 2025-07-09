# else and finally usage
try:
    age = int(input("Enter your age: "))
    print("You're", age, "years old.")
except ValueError:
    print("❌ Invalid age input.")
else:
    print("✅ Input was successfully processed.")
finally:
    print("✅ Program execution complete.")