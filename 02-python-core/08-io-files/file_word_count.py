# Count lines, words, and characters in a file
with open("example.txt", "r") as file:
    content = file.read()

lines = content.split('\n')
words = content.split()
characters = len(content)

print("📊 File Statistics:")
print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)