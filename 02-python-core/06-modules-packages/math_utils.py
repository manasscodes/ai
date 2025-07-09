# math_utils.py
def add(a, b):
    return a + b

def square(n):
    return n * n

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)