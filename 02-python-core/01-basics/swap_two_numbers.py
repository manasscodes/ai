# Swap two variables without using a third variable
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

a, b = b, a

print("After swapping: a =", a, ", b =", b)