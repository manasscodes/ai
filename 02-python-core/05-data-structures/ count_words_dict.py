# Count word frequency in a string
sentence = "ai is the future and ai will lead the future"
words = sentence.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")