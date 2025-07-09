# Using custom package modules
from package_demo.geometry import area_of_circle, perimeter_of_square
from package_demo.conversion import km_to_miles, celsius_to_fahrenheit

print("Area of circle (r=7):", area_of_circle(7))
print("Perimeter of square (side=4):", perimeter_of_square(4))
print("10 km in miles:", km_to_miles(10))
print("25°C in Fahrenheit:", celsius_to_fahrenheit(25))