# Using with open() context manager
with open("example.txt", "r") as file:
    lines = file.readlines()

print("📚 Lines from file:")
for line in lines:
    print(line.strip())