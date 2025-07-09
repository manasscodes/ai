# Print even or odd numbers from 1 to N
n = int(input("Enter a number: "))
print("Even numbers from 1 to", n, ":")

for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=" ")