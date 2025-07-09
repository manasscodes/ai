# Function that accepts another function
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

def cube(x):
    return x ** 3

print("Square of 5:", apply_function(square, 5))
print("Cube of 3:", apply_function(cube, 3))