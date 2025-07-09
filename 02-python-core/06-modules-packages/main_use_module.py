# Importing and using custom modules
import math_utils as mu
from string_utils import is_palindrome, count_vowels

print("Add 5 + 3:", mu.add(5, 3))
print("Square of 6:", mu.square(6))
print("Factorial of 5:", mu.factorial(5))

word = "Radar"
print(f"Is '{word}' a palindrome?:", is_palindrome(word))
print(f"Number of vowels in '{word}':", count_vowels(word))