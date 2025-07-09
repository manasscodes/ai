# Dictionary CRUD operations
student = {
    "name": "Manas",
    "age": 21,
    "track": "AI"
}

student["age"] = 22         # Update
student["email"] = "manas@example.com"  # Add
del student["track"]        # Delete

print("Student Info:")
for key, value in student.items():
    print(f"{key}: {value}")