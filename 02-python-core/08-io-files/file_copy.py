# Copy content from one file to another
with open("example.txt", "r") as source:
    content = source.read()

with open("copy_of_example.txt", "w") as target:
    target.write(content)

print("✅ File copied successfully.")